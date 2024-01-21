FROM gcr.io/oss-fuzz-base/base-builder
RUN apt-get update && apt-get install -y autoconf libtool texinfo

WORKDIR $SRC
COPY libredwg $SRC/libredwg
COPY llvmfuzz_seed_corpus.zip $SRC/llvmfuzz_seed_corpus.zip
COPY build.sh $SRC/build.sh
COPY llvmfuzz.options $SRC/llvmfuzz.options