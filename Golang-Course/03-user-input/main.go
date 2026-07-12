package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	welcome := "Welcome to user input"
	fmt.Println(welcome)

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter the rating for our pizza:")

	// Comma OK Sytax or Err Ok syntax

	rating, _ := reader.ReadString('\n')
	fmt.Println("Thanks for the rating:", rating)
	fmt.Printf("Type of this rating is: %T \n", rating)

}
