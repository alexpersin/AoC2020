package main

// read each line, regex parse into arguments
// create node if not exists, add to map
// add contains connections between nodes
// start at gold bag, add parents to set.
// continue recursively on parents if not already in set

struct Node {
	parents 
}

func main(){
	scanner := bufio.NewScanner(os.Stdin)

	bags := make(map[string]Node)

	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		instructions[i] = line
		i++
	}
}