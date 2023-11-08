package main

import "fmt"

func main() {
	defer FirstRun()
	SecondRun()
}

func FirstRun() {

	fmt.Println("I executed First.")
}

func SecondRun() {

	fmt.Println("I executed Second.")
}

func test() {
	fmt.Println(div(3, 0))
	fmt.Println(div(3, 5))
	demoPanic()
}

func div(num1, num2 int) int {
	defer func() {
		fmt.Println(recover())
	}()
	solution := num1 / num2

	return solution

}

func demoPanic() {
	defer func() {
		fmt.Println(recover())
	}()
	panic("Panic")
}

func demo() {
	fmt.Println(addemup(10, 20, 30, 40, 50))
}

func addemup(args ...int) int {
	sum := 0

	for _, value := range args {
		sum += value // the sum is equal to the sum plus the value
	}
	return sum
}
