package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// Read the file, iterate over it increasing the index into each line
func main() {
	file, err := os.Open("inputs/3")
	// check(err)
	defer file.Close()

	i := 0
	r := 1
	count := 0
	ln := 0
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
		ln++
		if ln%2 == 0 {
			continue
		}
		if string(line[i]) == "#" {
			count++
		}
		i += r
		i = i % (len(line) - 1)
	}
	fmt.Println(count)
}
