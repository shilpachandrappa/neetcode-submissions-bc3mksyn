class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_map = { }
        for i , num in enumerate(nums2):
            num2_map[num] = i
        for i, num in enumerate(nums1) :
            if num in num2_map :
                nums1[i] = num2_map[num]
        return nums1
