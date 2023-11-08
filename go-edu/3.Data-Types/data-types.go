// Numeric - int (also of ints and unsigned ints) and float
// String - string literals
// Boolean - True, False
// Derived - Pointer, Array, Structure, Map, Interface
package main

import "fmt"

func main() {
	var a int = 5
	var b float32 = 4.32
	const pi float64 = 3.121

	x, y := 14, 15

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(pi)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(x, y)
}
