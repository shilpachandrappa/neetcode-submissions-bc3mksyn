class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        char_count = Counter(nums)
        max_num = -1
        for element, count in char_count.items():
            if count == 1 :
                max_num= max(max_num, element)
        return max_num