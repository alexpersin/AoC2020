// ways to get to n equals the sum of ways to get to n-1..n-3
// cat inputs/10 | sort -n | go run 10/main.go | tail -1

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	a := make([]uint64, 200)
	a[2] = 1

	for scanner.Scan() {
		l, _ := strconv.Atoi(scanner.Text())
		a[l+3] = a[l+2] + a[l+1] + a[l]
		fmt.Println(a[l+3])
	}
}
