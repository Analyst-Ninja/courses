package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println("Welcome to the tutorial on Slices")

	// Initializing the slice with values
	var fruitList = []string{"Apple", "Banana", "Peach"}
	fmt.Println("fruitList: ", fruitList)
	fmt.Printf("Type of the fruitList is %T\n", fruitList)
	fmt.Println("Length: ", len(fruitList))

	// In slicers we can't assigned value like in Array
	// for eg. fruitList[0] = "Apple" a big no 🚫
	// Instead we use append
	fruitList = append(fruitList, "Mango", "Orange")
	fmt.Println("fruitList: ", fruitList)
	fmt.Println("Length: ", len(fruitList))

	// Slicing
	fruitList = append(fruitList[1:3]) // Slicing the slice fruitList
	fmt.Println("This is a fruitList", fruitList)
	fmt.Println("Length: ", len(fruitList))

	// Another way to initialize slice
	highScores := make([]int, 4)

	highScores[0] = 12
	highScores[1] = 13
	highScores[2] = 14
	highScores[3] = 15

	// highScores[4] = 123 // index of range error

	// but in append case, it will re allocate the memory
	highScores = append(highScores, 112, 23, 121, 1212)

	fmt.Println(sort.IntsAreSorted(highScores)) // Check if Int slice is sorted --> false
	sort.Ints(highScores)                       // Sort the slices of Int
	fmt.Println(highScores)
	fmt.Println(sort.IntsAreSorted(highScores))

	// ------ how to remove value from slices based on index ------

	var courses = []string{"React.js", "JavaScript", "Python", "RubyOnRails", "C++"}
	fmt.Println("Courses Slices:", courses)

	// Remove the value at the index specified
	var index int = 2
	courses = append(courses[:index], courses[index+1:]...)
	fmt.Println("New List of Courses:", courses)
}
