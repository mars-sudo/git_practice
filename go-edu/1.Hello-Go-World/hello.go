// https://www.youtube.com/watch?v=Q0sKAMal4WQ
package main

import "fmt"

func main() {
	fmt.Println("Hello World! This is my first go program!")
}

// go run is like running your program like a script, for example - go run hello.go
// go build is turning your program into an executable, for example - go build hello.go
// The Go development tools include a command, go fmt, which automatically reformats your code to match the standard format.
// go fmt hello.go
// An enhanced version of go fmt is call goimports, this also cleans up your import statements.
// You can run it across a project with the command goimports -l -w .
// The -l flag tells imports to print the files with incorrect formatting to the console, -w tells imports to modify the file in-place.
// goimports -l -w hello.go

// Always run go fmt or goimports

// Open gitbash, and run golangci-lint run hello.go
// You can use go vet as a required part of automated build process
// and golangci-lint as part of the code review process.
