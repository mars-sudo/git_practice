package main

import "fmt"

// Structures in go allow you to define variables that can hold several data items of the same kind
func main() {

	rect1 := Rectangle{10, 5}
	fmt.Println(rect1.height)
	fmt.Println(rect1.width)
	fmt.Println("The Area of the rectangle is ", rect1.area())
}

type Rectangle struct {
	height float64
	width  float64
}

func (rect *Rectangle) area() float64 {

	return rect.width * rect.height
}

// A Structure is another user defined data type available
// in go programming which allows you to combine data items
// of different kinds.
// The structures are used to represent a record.

// Suppose you want to keep track of the books
// in the library you might to track the following
// attributes like title, author, subjec, etc.
// In such a scenario structures are useful.
