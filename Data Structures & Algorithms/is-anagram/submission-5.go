func isAnagram(s string, t string) bool {


    map1 := createMapping(s)
    map2 := createMapping (t)

    return checkEquality (map1, map2)

}

func createMapping (s string) map[rune]int {
    mapping := make(map[rune]int)

    for _,char := range s {
        mapping[char]++
    }

    return mapping
}

func checkEquality (s map[rune]int, t map[rune]int) bool {
    if len (s) != len (t) {
        return false
    }

    for char, count := range s {
        
        //check the existience in the other
        value, ok := t[char]

        if !ok {
            return false
        }

        if  count != value {
            return false
        }
    }

    return true

}
