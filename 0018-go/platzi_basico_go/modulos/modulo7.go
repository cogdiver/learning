package modulos

import (
	"fmt"
	"sync"
	// "time"
)

func say(text string, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println(text)
}

func Modulo7() {
	var wg sync.WaitGroup
	
	fmt.Println("Hello")
	wg.Add(2)
	
	go say("world", &wg)

	go func(text string, wg *sync.WaitGroup) {
		defer wg.Done()
		fmt.Println(text)
	}("Bye", &wg)

	wg.Wait()

	// time.Sleep(1 * time.Second)
}
