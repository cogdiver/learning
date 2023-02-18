package mypackage

import "fmt"

// CarPublic
type CarPublic struct {
	Brand string
	Year  int
}

type carPrivate struct {
	Brand string
	Year  int
}

func PrintMessage(message string) {
	fmt.Println(message)
}
