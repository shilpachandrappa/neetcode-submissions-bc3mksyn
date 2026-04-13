class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        left , right = 0, 1
        while right < len(nums) :
            if nums[left] != nums[right]:
                right += 1
                left += 1
            else :
                nums.pop(right)
                
        return left+1