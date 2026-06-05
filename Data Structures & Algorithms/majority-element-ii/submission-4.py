class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_arr = Counter(nums)
        print(count_arr)
        result = []
        for value, count in count_arr.items() :
            if count > len(nums)//3 :
                result.append(value) 
        return result