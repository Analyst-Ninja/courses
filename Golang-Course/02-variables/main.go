package main

import "fmt"

const LoginToken string = "asjkcbasbclkasbkl" // Public

// jwtToken := 982689689 // --> This way to assign the variable is not allow outside a method or Globally

var jwtToken string = "ascjbaslkcb;anpcawlks;cn;wa" // Assigning variable by this way is allowed

func main() {
	var username string = "Rohit"
	fmt.Println(username)
	fmt.Printf("Variable is of Type: %T \n", username)

	var isLoggedIn bool = true
	fmt.Println(isLoggedIn)
	fmt.Printf("Variable is of Type: %T \n", isLoggedIn)

	var smallValue uint8 = 255
	fmt.Println(smallValue)
	fmt.Printf("Variable is of Type: %T \n", smallValue)

	var smallFloat float32 = 255.3289498329869869869869869869
	fmt.Println(smallFloat)
	fmt.Printf("Variable is of Type: %T \n", smallFloat)

	// Default Values and Aliases
	var anotherVariable int
	fmt.Println(anotherVariable)
	fmt.Printf("Variable is of Type: %T \n", anotherVariable)

	// Implicit Type Style
	var website = "go.dev" // Implicitly take the type as string
	fmt.Println(website)
	// website = 3 --> Can't change the type once type is assigned

	// no var Style
	numberOfUsers := 201
	fmt.Println(numberOfUsers)
	numberOfUsers = 213123123123128
	fmt.Println(numberOfUsers)

	fmt.Println(jwtToken)

	fmt.Println(LoginToken)
	fmt.Printf("Variable is of Type: %T \n", LoginToken)

}
