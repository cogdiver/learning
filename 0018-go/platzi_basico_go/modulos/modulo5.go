package modulos

import "fmt"

type pc struct {
	ram   int
	disk  int
	brand string
}

func (myPC pc) ping() {
	fmt.Println(myPC.brand, "P")
}

func (myPC *pc) duplicateRAM() {
	myPC.ram = myPC.ram * 2
}

func (myPC pc) String() string {
	return fmt.Sprintf("%d GB RAM, %d GB Discom, %s Marca", myPC.ram, myPC.disk, myPC.brand)
}

func Modulo5() {
	// Punteros
	a := 50
	b := &a

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(*b)

	*b = 100
	fmt.Println(a)

	myPC := pc{16, 200, "MSI"}
	fmt.Println(myPC)
	myPC.ping()

	fmt.Println(myPC)
	myPC.duplicateRAM()
	fmt.Println(myPC)
	myPC.duplicateRAM()
	fmt.Println(myPC)

}
