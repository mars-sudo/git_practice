package main

import "fmt"

func main() {

	var age int = 18

	if age > 18 {
		print("you can vote")
	} else {
		fmt.Println("No, you can't vote")
	}

	SwitchStatement()
}

func SwitchStatement() {

	amount := 20

	switch amount {
	case 19:
		fmt.Println("need one more item")
	case 20:
		fmt.Println("enough items to purchase")
	case 21:
		fmt.Println("to many items to hold")
	default:
		fmt.Println("default statement amount")
	}

}
