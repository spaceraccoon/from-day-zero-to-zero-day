{
  onEnter(log, args, state) {
    log(`system(command="${args[0].readUtf8String()}")`);
    args[0].writeUtf8String('modified argument!');
    log(`system(command="${args[0].readUtf8String()}")`);
  },

  onLeave(log, retval, state) {
    log(`system returned ${retval}`);
  }
}