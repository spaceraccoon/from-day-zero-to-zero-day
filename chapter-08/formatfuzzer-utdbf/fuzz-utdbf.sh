#!/usr/bin/env bash

while true
do
  ./dbf-fuzzer fuzz test.dbf 2>/dev/null
  # run utdbf for maximum 1 second on test case and exit
  timeout 1 ../utdbf/utdbf ./test.dbf <<< "0" >/dev/null
  test $? -gt 127 && break
done