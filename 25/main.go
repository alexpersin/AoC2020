// tryLoop(n, 7) == cardPK
// tryLoop(n, doorPK) == answer

package main

import "fmt"

func encrypt(loopNum, subject int) int {
	n := 1
	for i := 0; i < loopNum; i++ {
		n *= subject
		n = n % 20201227
	}
	return n
}

func main() {
	cardPK := 3469259
	doorPK := 13170438

	// sample
	// cardPK = 5764801
	// doorPK = 17807724

	var secretLoopNum int
	n := 1
	subject := 7
	for i := 1; i < 10000000000; i++ {
		n *= subject
		n = n % 20201227
		if n == cardPK {
			secretLoopNum = i
			break
		}
	}
	if secretLoopNum == 0 {
		fmt.Println("Failed")
	} else {
		fmt.Println(secretLoopNum)
		fmt.Println(encrypt(secretLoopNum, doorPK))
	}
}
