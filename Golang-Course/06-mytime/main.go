package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Welcome, Lets learn time module")

	presentTime := time.Now()
	fmt.Println(presentTime)

	fmt.Println(presentTime.Format("02-01-2006 15:04:05 Monday"))

	createDate := time.Date(2025, time.February, 8, 18, 06, 23, 0, time.UTC)
	fmt.Println(createDate)
	fmt.Println(createDate.Format("01-02-2006 15:04:05 Monday"))
}
