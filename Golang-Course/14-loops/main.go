package main

import "fmt"

func main() {
	fmt.Println("Loops in golang")

	days := []string{"Sunday", "Tuesday", "Wednesday", "Friday", "Saturday"}
	fmt.Println("days in slice:", days)

	// In Golang, there is only FOR LOOPS for looping
	// For Loop: type 1 // like for loop in C
	for i := 0; i < len(days); i++ { // in golang, only i++ is there no ++i
		fmt.Println("day:", days[i])
	}

	// For Loop: type 2 --> like for i in range(len(days)) [Python]
	for i := range days { // range --> returns indexes, unlike in python it returns values in iterator
		fmt.Println("day:", days[i])
	}

	// For Loop: type 3 --> like for day in days: [Python]
	for index, day := range days {
		fmt.Printf("index: %v day: %v\n", index, day)
	}
	for _, day := range days {
		fmt.Printf("day: %v", day)
	}

	// For Loop: type 4 --> like while loop
	rougueValue := 1

	for rougueValue < 10 {
		fmt.Println("Rougue Value is:", rougueValue)
		rougueValue++
	}

	// Break and continue statement

	// Break
	for rougueValue < 10 {
		if rougueValue == 3 {
			goto lco
		}
		if rougueValue == 5 {
			break
		}
		fmt.Println("Rougue Value is:", rougueValue)
		rougueValue++
	}

	// continue
	for rougueValue < 10 {
		if rougueValue == 5 {
			rougueValue++ // skip 1 value so we dont keep loop running for targetValue
			continue
		}
		fmt.Println("Rougue Value is:", rougueValue)
		rougueValue++
	}

	// GOTO statement

	// Assigning label for GOTO --> lco
lco:
	fmt.Println("Jumping at -> www.learncodeonline.com")
}
