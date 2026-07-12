package main

import "fmt"

func main() {
	fmt.Println("Welcome to pointers tutorial")

	// var ptr *int
	// fmt.Println("Value of the pointer (uninitialized with value) is:", ptr)

	myNum := 23

	var ptr = &myNum // --> & for referencing
	fmt.Println("Value of actual pointer is:", ptr)
	fmt.Println("Value of actual pointer is:", *ptr) // * --> for the getting the value

	*ptr = *ptr * 2 // Multiplying by 2

	fmt.Println("New Value is:", myNum)
}
