package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

// read each line, regex parse into arguments
// create node if not exists, add to map
// add contains connections between nodes
// start at gold bag, add parents to set.
// continue recursively on parents if not already in set

type Node struct {
	key string
}

func NewNode(key string) *Node {
	return &Node{
		key: key
	}
}

type Graph struct {
	nodes []*Node
	edges map[string][]*Node
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	r, _ := regexp.Compile(`^(\w+ \w+) bags contain (\d+ \w+ \w+ \w+)*,* *(\d+ \w+ \w+ \w+)*,* *(\d+ \w+ \w+ \w+)*,* *(\d+ \w+ \w+ \w+)*\.*$`)
	// r, _ := regexp.Compile(`.*bags contain).*`)
	// bags := make(map[string]Node

	for scanner.Scan() {
		line := scanner.Text()
		m := r.FindAllStringSubmatch(line, -1)
		fmt.Println(line)
		if len(m) > 0 {
			for _, x := range m[0] {
				fmt.Println(x)
			}
			fmt.Println("\n")
		}
	}
}
