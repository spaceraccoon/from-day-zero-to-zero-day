/**
 * @id integer-overflow-allocation-size
 * @name Integer Overflow in Allocation Size
 * @description Potential integer overflow passed to allocation size.
 * @kind path-problem
 * @severity error
 */

import cpp
import semmle.code.cpp.rangeanalysis.SimpleRangeAnalysis
import semmle.code.cpp.dataflow.new.DataFlow
import DataFlow::PathGraph

class MyConfig extends DataFlow::Configuration {
  MyConfig() { this = "MyConfig" }

  override predicate isSource(DataFlow::Node source) {
    exists(Expr e | e = source.asExpr() |
      (
        e instanceof UnaryArithmeticOperation or
        e instanceof BinaryArithmeticOperation or
        e instanceof AssignArithmeticOperation
      ) and
      convertedExprMightOverflow(e)
    )
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(Expr e, ExprCall ec, MacroInvocation mi | e = sink.asConvertedExpr() |
      ec = mi.getExpr() and
      mi.getMacroName() = "REALLOC" and
      e = ec.getAnArgument() and
      e.getUnspecifiedType() instanceof IntegralType
    )
  }
}
 
from MyConfig cfg, DataFlow::PathNode source, DataFlow::PathNode sink
where cfg.hasFlowPath(source, sink)
select sink, source, sink, 
"Potential integer overflow $@ passed to allocation size $@.", source, "source", sink, "sink"