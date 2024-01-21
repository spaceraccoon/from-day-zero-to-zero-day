#include <dwg.h>
#include "bits.h"
#include "decode.h"

extern int LLVMFuzzerTestOneInput (const uint8_t *data, size_t size);

int LLVMFuzzerTestOneInput (
  const uint8_t *data, size_t size
) {
  Dwg_Data dwg;
  Bit_Chain dat = { NULL, 0, 0, 0, 0 };

  memset(&dwg, 0, sizeof (dwg));  
  dat.chain = (unsigned char *)data;
  dat.size = size;

  dwg_decode(&dat, &dwg);
  dwg_free(&dwg);

  return 0;
}