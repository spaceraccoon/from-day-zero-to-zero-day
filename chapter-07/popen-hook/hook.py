import threading

from frida_tools.application import Reactor

import frida
import sys

SCRIPT = """
Interceptor.attach(Module.getExportByName(null, 'popen'), {
  onEnter: function (args) {
    send({
      function: 'popen',
      command: Memory.readUtf8String(args[0]),
    });
  }
});
"""

class Application:
    def __init__(self, argv, script):
        self._argv = argv
        self._script = script
        self._stop_requested = threading.Event()
        self._reactor = Reactor(
            run_until_return=lambda reactor: self._stop_requested.wait()
        )


    def run(self):
        self._reactor.schedule(lambda: self._start())
        self._reactor.run()

    def _start(self):
        pid = frida.spawn(self._argv)
        session = frida.attach(pid)
        session.on(
            "detached",
            lambda reason: self._reactor.schedule(
                lambda: self._on_detached(pid, session, reason)
            )
        )
        script = session.create_script(self._script)
        script.on("message", self._on_message)
        script.load()
        frida.resume(pid)

    def _on_message(self, message, data):
        print(message)

    def _stop_if_idle(self):
    	self._stop_requested.set()

    def _on_detached(self, pid, session, reason):
        self._reactor.schedule(self._stop_if_idle, delay=0.5)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python hook.py <command>")
        exit(1)
        
    app = Application(sys.argv[1:], SCRIPT)
    app.run()