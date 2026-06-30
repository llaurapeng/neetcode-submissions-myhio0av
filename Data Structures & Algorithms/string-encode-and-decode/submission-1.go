

type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    var ret strings.Builder

    for _, str := range strs {
        length := strconv.Itoa(len(str))

        ret.WriteString(length)
        ret.WriteString("#")
        ret.WriteString(str)
    }
    return ret.String()
}

func (s *Solution) Decode(encoded string) []string {
	result := []string{}
	i := 0

	for i < len (encoded) {
		// find the #
		j:=i
		for encoded[j] != '#' {
			j++
		}

		// get the length number
		lengthStr := encoded [i:j]

		length,_ :=strconv.Atoi(lengthStr)

		//move past #
		j++

		word := encoded [j:j+length]
		result = append (result, word)

		i = j+length
	}

	return result

}
