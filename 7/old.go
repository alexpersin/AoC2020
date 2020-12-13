// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"strings"
// )

// // read each line, regex parse into arguments
// // create node if not exists, add to map
// // add contains connections between nodes
// // start at gold bag, add parents to set.
// // continue recursively on parents if not already in set

// // struct Node {
// // 	parents
// // }

// func main() {
// 	scanner := bufio.NewScanner(os.Stdin)
// 	// bags := make(map[string]Node)

// 	for scanner.Scan() {
// 		line := scanner.Text()
// 		l := strings.Split(line, "contain")
// 		outer := l[0]
// 		var inner []string
// 		for i, p := range strings.Split(l[1], ",") {
// 			a := strings.SplitN(p, " ", 1)
// 		}
// 		fmt.Println(outer)
// 		fmt.Println(s)
// 	}
// }
