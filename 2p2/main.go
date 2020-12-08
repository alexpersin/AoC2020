package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func valid(min, max uint64, char byte, pwd string) bool {
	x := pwd[min-1] == char
	y := pwd[max-1] == char
	return (x || y) && !(x && y)
}

func main() {
	file, err := os.Open("input1")
	check(err)
	defer file.Close()

	ans := 0
	reader := bufio.NewReader(file)
	var line string
	for {
		line, err = reader.ReadString('\n')
		if err != nil && err != io.EOF {
			break
		}
		if len(line) == 0 {
			break
		}

		parts := strings.Split(line, " ")
		mm := strings.Split(parts[0], "-")
		min, _ := strconv.ParseUint(mm[0], 10, 64)
		max, _ := strconv.ParseUint(mm[1], 10, 64)
		char := parts[1][0]
		pwd := parts[2]
		// fmt.Println(min, max, char, pwd)
		// fmt.Println(valid(min, max, char, pwd))
		if valid(min, max, char, pwd) {
			ans++
		}
	}
	fmt.Println(ans)
}
