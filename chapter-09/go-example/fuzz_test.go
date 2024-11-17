package main

import (
    "net/url"
    "strings"
    "testing"
)

func FuzzValidateURLDomain(f *testing.F) {
    // Add seed corpus.
    f.Add("https://example.com")
    domain := "example.com"
    f.Fuzz(func(t *testing.T, data string) {
        parsedURL, err := url.Parse(data)
        if (err == nil) {
            host := strings.ToLower(parsedURL.Host)
            if (ValidateURLDomain(data, domain) && host != domain &&
                !strings.HasSuffix(host, "."+domain)) {
                t.Errorf("Incorrectly validated %q", data)
            }
        }
    })
}