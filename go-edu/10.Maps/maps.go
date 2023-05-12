package main

import "fmt"

// Maps is basically a dictionary, provides a key value pair
// data structure.
func main() {
	Student := make(map[string]int)
	Student["Mars"] = 30
	fmt.Println(Student["Mars"])
	fmt.Println(len(Student))

	Student["Artemis"] = 28
	fmt.Println(len(Student))
	delete(Student, "Mars")
	fmt.Println(len(Student))

	map_practice()

	map_in_map()

}

func map_practice() {
	StudentAge := make(map[string]int)

	StudentAge["Bethany"] = 22
	StudentAge["Hector"] = 25
	StudentAge["Emily"] = 30
	StudentAge["Kai"] = 45

	fmt.Println(StudentAge["Emily"])
	fmt.Println(len(StudentAge))

}

func map_in_map() {

	superhero := map[string]map[string]string{

		"Superman": map[string]string{
			"RealName": "Clark Kent",
			"City":     "Metropolis",
		},

		"Batman": map[string]string{
			"RealName": "Bruce Wayne",
			"City":     "Gotham City",
		},
	}

	if temp, hero := superhero["Superman"]; hero {
		fmt.Println(temp["RealName"], temp["City"])
	}

}
