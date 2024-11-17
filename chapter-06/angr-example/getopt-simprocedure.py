import angr
import claripy
import archinfo


class GetOptHook(angr.SimProcedure):
    def run(self, argc, argv, optstr):
        # emulate extern variable optind that's the index of the next
        # element in argv to be processed
        try:
            self.state.globals["optind"] += 1
        except KeyError:
            self.state.globals["optind"] = 1

        strlen = angr.SIM_PROCEDURES["libc"]["strlen"]

        # load null-byte separated argv array buffer
        argv_buf = self.state.memory.load(
            argv, self.state.arch.bytes, endness=self.arch.memory_endness
        )

        # get expression of value at argv[optind]
        for i in range(self.state.globals["optind"]):
            argv_elem_len = self.inline_call(strlen, argv_buf)
            argv_buf += argv_elem_len.max_null_index + 1

        argv_elem_len = self.inline_call(strlen, argv_buf)
        argv_elem_expr = self.state.memory.load(
            argv_buf, argv_elem_len.max_null_index, endness=archinfo.Endness.BE
        )

        # get evaluated value of optstring
        optstr_len = self.inline_call(strlen, optstr)
        optstr_expr = self.state.memory.load(
            optstr, optstr_len.max_null_index, endness=archinfo.Endness.BE
        )
        optstr_val = self.state.solver.eval(optstr_expr, cast_to=bytes)

        # case 1: argv element value is concrete, perform simple search for 
        # '-<VALID OPTION CHAR>' prefix
        if argv_elem_expr.concrete:
            argv_elem_val = self.state.solver.eval(argv_elem_expr, cast_to=bytes)
            for optkey in optstr_val.strip(b":"):
                if argv_elem_val[0] == ord(b"-") and argv_elem_val[1] == optkey:
                    return optkey
        # case 2: argv element value is symbolic, add conditions based on optstr
        else:
            or_expressions = []
            for optkey in optstr_val.strip(b":"):
                or_expressions.append(argv_elem_expr.get_byte(1) == optkey)

            # if argv element value prefix matches '-<VALID OPTION CHAR>', 
            # evaluate to <VALID OPTION CHAR>, else '?'
            return self.state.solver.If(
                self.state.solver.And(
                    argv_elem_expr.get_byte(0) == b"-",
                    self.state.solver.Or(*[c for c in or_expressions]),
                ),
                argv_elem_expr.get_byte(1),
                ord("?"),
            )

        # concerete argv value does not match a '-<VALID OPTION CHAR>' so
        # return '?'
        return ord("?")


proj = angr.Project("httpd", auto_load_libs=False)
proj.hook_symbol("getopt", GetOptHook())

# add command-line option symbol of length 12
argv1 = claripy.BVS("argv1", 12 * 8)

# insert symbol into simulation as command-line option
state = proj.factory.entry_state(args=["./httpd", argv1])
simgr = proj.factory.simulation_manager(state)

# execute until instruction address within options parsing block
simgr.explore(find=0x405184)

# print evaluated value of argv1 at found state
found = simgr.found[0]
print(found.solver.eval(argv1, cast_to=bytes))
print(found.solver.constraints)