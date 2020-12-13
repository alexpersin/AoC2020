cat inputs/10 | sort -n | tail -1 >> inputs/10
cat inputs/10 | sort -n | awk '{print $0 - prev} { prev = $0 }' | sort | uniq -c