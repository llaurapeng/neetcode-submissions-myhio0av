func hasDuplicate(nums []int) bool {

    values := make(map[int]int)

    for _, num := range nums {

        value, ok := values [num]

        if !ok {
            // value not found
            values [num] = 0
        }
        
        values [num] = value + 1
        

    }

    for _, count := range values {
        if count > 1 {
            return true
        }
    }

    return false

}
