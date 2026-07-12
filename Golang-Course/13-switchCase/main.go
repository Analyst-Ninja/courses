package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("Dice Game")

	rand.Seed(time.Now().UnixNano())
	diceNumber := rand.Intn(6) + 1
	fmt.Println("dice number:", diceNumber)

	switch diceNumber {
	case 1:
		fmt.Println("Dice Value is 1, you can open or move 1 spot")
	case 2:
		fmt.Println("You can move 2 spots")
	case 3:
		fmt.Println("You can move 3 spots")
		fallthrough // will run this statement and also run the next one as well
	case 4:
		fmt.Println("You can move 4 spots")
		fallthrough //
	case 5:
		fmt.Println("You can move 5 spots")
	case 6:
		fmt.Println("You can move 6 spots and roll the dice again")
	default:
		fmt.Println("What was that!!")
	}

}
