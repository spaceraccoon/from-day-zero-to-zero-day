/**
 * @id remote-command-injection
 * @name Remote Command Injection
 * @description Passing user-controlled remote data to a command injection.
 * @kind path-problem
 * @severity error
 */

import javascript

module RemoteCommandInjectionConfig implements DataFlow::ConfigSig { 
    predicate isSource(DataFlow::Node source) {
        source instanceof RemoteFlowSource
    }

    predicate isSink(DataFlow::Node sink) {
        sink = any(SystemCommandExecution sys).getACommandArgument()
    }
}

module RemoteCommandInjectionFlow = TaintTracking::
    Global<RemoteCommandInjectionConfig>;

import RemoteCommandInjectionFlow::PathGraph

from RemoteCommandInjectionFlow::PathNode source,
    RemoteCommandInjectionFlow::PathNode sink
where RemoteCommandInjectionFlow::flowPath(source, sink)
select sink.getNode(), source, sink,
    "taint from $@ to $@.", source.getNode(), "source", sink, "sink"