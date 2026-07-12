package main

import "fmt"

func main() {
	fmt.Println("Functions in golang")
	greet()

	// Not Allowed to define functions inside a function
	// func greetTwo()  {
	// 	fmt.Println("Good Morning")
	// }

	// greetTwo()

	result := adder(3, 4)
	fmt.Println("Added value:", result)

	proResult, message := proAdder(1, 2, 2, 3, 3, 4, 4)
	fmt.Println("Added through proAdder:", proResult)
	fmt.Println("Message through proAdder:", message)
}

func greet() {
	fmt.Println("Namaste from golang")
}

func adder(a int, b int) int {
	res := a + b
	return res
}

func proAdder(values ...int) (int, string) {
	total := 0
	for _, val := range values {
		total += val
	}
	return total, "proAdder function"
}
