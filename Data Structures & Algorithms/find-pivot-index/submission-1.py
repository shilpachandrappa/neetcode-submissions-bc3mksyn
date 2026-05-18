class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        curSum = 0
        for i , num in enumerate(nums):
            if curSum == (totalSum - curSum - num) :
                return i 
            curSum += num
            #print(curSum)
            #print(totalSum - curSum)
            
        return -1