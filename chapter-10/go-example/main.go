package main

import (
	"fmt"
	"regexp"
)

// Validates whether inputURL is a domain or subdomain of expectedDomain.
func ValidateURLDomain(inputURL string, expectedDomain string) bool {
	// Escapes special characters in expectedDomain.
	expectedDomain = regexp.QuoteMeta(expectedDomain)

	regexPattern := `^https?://(?:[A-Za-z0-9-]+.)*` + expectedDomain + 
		`($|/|\?)`

	regex, err := regexp.Compile(regexPattern)
	if err != nil {
		return false
	}

	return regex.MatchString(inputURL)
}

func main() {
	// Returns true.
	fmt.Println(ValidateURLDomain("https://example.com", "example.com"))
	// Returns true.
	fmt.Println(ValidateURLDomain("https://sub.example.com", "example.com"))
	// Returns false.
	fmt.Println(ValidateURLDomain("https://evil.com", "example.com"))
}