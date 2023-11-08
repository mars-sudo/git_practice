package main

import "fmt"

func main() {
	x := 5

	fmt.Println(x)  //This prints the value
	fmt.Println(&x) //This is the address that the value is stored

	changeValue(&x)
	fmt.Println(x)
}

func changeValue(x *int) {
	*x = 7

}
