while true
do
  radamsa test/files/test2.xls > fuzzed.xls
  ./test2_libxls fuzzed.xls > /dev/null
  test $? -gt 127 && break
done