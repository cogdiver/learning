package modulos

import (
	"fmt"
	"sync"
)

var balance int = 100

// func Deposit(amount int, wg *sync.WaitGroup) {
func Deposit(amount int, wg *sync.WaitGroup, lock *sync.RWMutex) {
	defer wg.Done()
	lock.Lock()
	b := balance
	balance = b + amount
	lock.Unlock()
}

func Balance(lock *sync.RWMutex) int {
	lock.RLock()
	b := balance
	lock.RUnlock()
	return b
}

func Modulo1() {

	var wg sync.WaitGroup
	// var lock sync.Mutex
	var lock sync.RWMutex

	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// go Deposit(i*100, &wg)
		go Deposit(i*100, &wg, &lock)
	}

	wg.Wait()
	fmt.Println(Balance(&lock))

}
