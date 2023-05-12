package main

import "fmt"

func main() {

	const pi float64 = 3.161
	x := 5
	isbool := true
	var name string = "Mr.Martin"

	// printf is formatted printing
	fmt.Printf(" %f \n", pi) //prints a float

	fmt.Printf(" %T \n", isbool) //prints the type

	fmt.Printf(" %b \n", x)

	fmt.Printf(" %b \n", 25) // prints the binary

	fmt.Printf(" %x \n", 15) // prints the hex code

	fmt.Printf(" %c \n", 34) // print the character associated with the ASCII code

	fmt.Printf(" %e \n", pi) // print in scientific notation

	fmt.Println(len(name))

	fmt.Println(name + " is a chill guy")
}
