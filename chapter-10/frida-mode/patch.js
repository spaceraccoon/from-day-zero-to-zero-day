const bit_check_CRC = DebugSymbol.fromName('bit_check_CRC').address;
Afl.print(`bit_check_CRC: ${bit_check_CRC}`);

const bit_check_CRC_replacement = new NativeCallback(
  (dat, start_address, seed) => {
    Afl.print('intercepted bit_check_CRC');
    Afl.print(`seed: ${seed}`);
    return 1;
  },
  'int',
  ['pointer', 'ulong', 'uint16']);
Interceptor.replace(bit_check_CRC, bit_check_CRC_replacement);

Afl.done();