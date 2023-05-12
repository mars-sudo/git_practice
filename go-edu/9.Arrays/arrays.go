// An Array is a collection of variables of the same type.
package main

import "fmt"

func main() {
	var StudentsCount [10]int

	for i := 0; i < 10; i++ {

		//StudentsCount[i] = i + 1
		StudentsCount[i] += 1
		fmt.Println(StudentsCount[i])
	}

	ArrayPrac1()
	ArrayPrac2()
}

func ArrayPrac1() {

	var EvenNum [5]int
	EvenNum[0] = 0 // this is one way to initialze an array
	EvenNum[1] = 2
	EvenNum[2] = 4
	EvenNum[3] = 6
	EvenNum[4] = 8

	fmt.Println(EvenNum[4])
}

func ArrayPrac2() {
	OddNum := [5]int{0, 1, 3, 5, 7}
	fmt.Println(OddNum[2])

	for _, value := range OddNum {
		fmt.Println(value)
	}

	for i, value := range OddNum {
		fmt.Println(value, i)
	}

	numSlice := []int{5, 4, 3, 2, 1}

	sliced := numSlice[0:3]
	fmt.Println(sliced)
	// Slicing is taking a subpart of the Array

	slice2 := make([]int, 5, 10)
	copy(slice2, numSlice)
	fmt.Println(numSlice)
}
