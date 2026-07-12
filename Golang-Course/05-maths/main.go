package main

import (
	"fmt"
	"math/big"

	// "math/rand"
	"crypto/rand"
)

func main() {
	fmt.Println("Welcome to maths in golang!!")

	// var numOne int = 4
	// var numTwo float64 = 6 // No need to write it as 6.0

	// fmt.Println("The sum is: ", numOne+numTwo) // Not allowed
	// fmt.Println("The sum is: ", numOne+int(numTwo)) // allowed --> We will be loosing precision here

	// Random Number --> Through math Package
	// rand.Seed(time.Now().UnixNano())
	// fmt.Println(rand.Intn(5) + 1)

	// Random Number --> Through crypto Package
	myRandomNum, _ := rand.Int(rand.Reader, big.NewInt(5))
	fmt.Println(myRandomNum)
}
