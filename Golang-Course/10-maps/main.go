package main

import (
	"fmt"
)

func main() {
	fmt.Println("Welcome to tutorial on maps")

	// maps --> Like a dictionary in python
	// keys --> can be anything
	// values --> can be anything

	// Initializing Map[TypeOfKey]TypeOfValue
	languages := make(map[string]string)
	languages["js"] = "JavaScript"
	languages["rb"] = "Ruby"
	languages["py"] = "Python"

	fmt.Println("Languages Map:", languages)
	fmt.Println("Selected Language:", languages["py"])

	// delete the value with key
	delete(languages, "rb")
	fmt.Println("Map after the deleting Ruby:", languages)

	// Loops
	for key, value := range languages {
		fmt.Printf("FOR key %v is %v\n", key, value)
	}

	// If we don't need the keys
	for _, value := range languages {
		fmt.Printf("FOR key %v\n", value)
	}

}
