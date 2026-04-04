class Solution:
    def sortColors(self, nums: List[int]) -> None:
        index = 0
        left , right = 0, len(nums)-1
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        while index <= right :
            if nums[index] == 0 :
                swap(index, left)
                left += 1
                index += 1
            elif nums[index] == 2:
                swap(index, right)
                right -= 1
            else :
                index += 1


# [2,0,2,1,1,0]
[0,0,1,2,1,2]

[0]