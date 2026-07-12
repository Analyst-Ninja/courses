package main

import "fmt"

func main() {
	fmt.Println("Conditionals (if else) in golang")

	loginCount := 10
	var result string

	if loginCount < 10 {
		result = "Regular User"
	} else if loginCount > 10 {
		result = "Watch Out"
	} else {
		result = "Exactly 10 login count"
	}

	fmt.Println("Result:", result)
	// For Web Request handling
	if num := 3; num > 10 {
		result = "Number > 10"
	} else if num < 10 {
		result = "Number < 10"
	} else {
		result = "Number = 10"
	}

	fmt.Println("Result:", result)
}
