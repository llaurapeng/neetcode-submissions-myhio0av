func twoSum(nums []int, target int) []int {
    mapping := make (map[int]int)

    for dex,num :=range nums {
        mapping [num] = dex
    }

    for dex,num :=range nums {
        need := target - num
        dex2, ok := mapping [need]

        if ok && dex != dex2 {
            //needed value is found
            return []int{dex,dex2}
        }
            
    }

    return nil

}
