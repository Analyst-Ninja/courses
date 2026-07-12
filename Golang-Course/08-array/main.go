package main

import "fmt"

func main() {
	fmt.Println("Welcome to Array in Golang!!")

	var fruitList [4]string

	fruitList[0] = "Apple"
	fruitList[1] = "Banana"
	fruitList[3] = "Peach"

	fmt.Println("Fruit list is:", fruitList)
	fmt.Println("Fruit list is:", len(fruitList))

	var vegList = [3]string{"Potato", "Beans", "Mushroom"}
	fmt.Println("Vegetable list is:", vegList)
	fmt.Println("Vegetable list is:", len(vegList))
}
