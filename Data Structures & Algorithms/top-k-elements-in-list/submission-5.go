func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int)

	for _,num := range (nums) {
		freq[num]++
	}

	//create a slice of okeys

	keys := []int{}

	for k := range freq {
		keys = append (keys, k)
	}

	sort.Slice (keys, func (i,j int) bool {
		return freq[keys[i]] > freq[keys[j]]
	})

	return keys[:k]
}
