package main

import "fmt"

func main() {
	fmt.Println("Hello World!")
}

//Control Structures for Functions

// Defer
// Defer statement defers the execution of a function until the surrounding function returns
// Multiple defers are pushed into stack and executes in Last In First Out (LIFO) order
// Defer genrally used to cleanup resources like file, database connection, etc.

// Recover
// Recover is another built-in funciton in go
// It helps to regain the normal flow of execution after a panic
// Generally its used with defer statement to recover panic in goroutine

// Panic
// Panic is similar to throwing exception like other language
// Generally when a panic is called then the normal execution flow is stopped immediately
// The deffered functions are executel normally
