// Types of Operators
// Arithmetic - addition (+), subtraction (-), multiplication (*), division (/), modulus (%)
// Relational - greater than (>), less than (<), greater than or equal (>=), equivalence(==), not equals(!=)
// Logical - and (&&), or (||), negation(!)

package main

import "fmt"

func main() {

	x, y := 5, 6

	fmt.Println(x, y)

	fmt.Println("x + y = ", x+y)
	fmt.Println("x - y = ", x-y)
	fmt.Println("x * y = ", x*y)
	fmt.Println("x / y = ", x/y)
	fmt.Println("x % y = ", x%y)

	// boolean
	isbool := true
	hate := false
	fmt.Println(isbool && hate)
	fmt.Println(isbool || hate)
	fmt.Println(!isbool)

}
