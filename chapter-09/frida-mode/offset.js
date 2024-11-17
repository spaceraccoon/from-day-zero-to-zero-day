const module = Process.getModuleByName('dwgread');
const dwg_read_file = module.base.add(0x059fe0);
Afl.setPersistentAddress(dwg_read_file);
Afl.done();