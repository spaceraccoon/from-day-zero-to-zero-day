package snappy

import (
    "testing"
)

func FuzzDecode(f *testing.F) {
    f.Fuzz(func(t *testing.T, data []byte) {
		var dst [1000000]byte
        decode(dst[:], data)
    })
}