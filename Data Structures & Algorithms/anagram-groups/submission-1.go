func groupAnagrams(strs []string) [][]string {
	// Map --> string: list
	helper := make(map[string][]string)

	for _,str := range strs {
		sorted := sortString (str)
		
		helper[sorted] = append (helper[sorted], str)
	}

	result := [][]string{}

	for _, val := range helper {
		result = append (result, val)
	}

	return result
}

func sortString (s string) string {
	//slice of runes (characters)
	//need the s because gives characters instead of bytes
	chars := []rune(s)

	sort.Slice (chars, func (i, j int) bool {
		return chars [i] < chars[j]

	})

	return string(chars)


}
