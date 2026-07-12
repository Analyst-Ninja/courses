package main

import "fmt"

func main() {
	fmt.Println("Welcome to tutorial on structs")

	// No inheritence in Golang // No super or parent

	// making a User struct
	rohit := User{"Rohit", "rohit@openai.com", true, 28}
	fmt.Println("Rohit Struct:", rohit)

	rohit.Name = "Rohit Kumar"

	// %+v --> This placeholder is used for details of a struct

	fmt.Printf("Details about %v are:%+v\n", rohit.Name, rohit)
}

// Defining struct
// struct name and variable are with capital as it can be accessed by anyonne
type User struct {
	Name   string
	Email  string
	Status bool
	Age    int
}
