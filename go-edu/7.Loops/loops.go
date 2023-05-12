package main

import "fmt"

func main() {
	for i := 1; i < 5; i++ {
		fmt.Println(i)
	}

	TestLoop()
	TestLoop2()
}

func TestLoop() {
	x := 2

	for x <= 10 {
		fmt.Println(x)
		x++
	}

}

func TestLoop2() {

	for y := 1; y < 5; y++ {

		for j := 1; j < y; j++ {
			fmt.Printf("*")
		}
		fmt.Println()
	}
}
