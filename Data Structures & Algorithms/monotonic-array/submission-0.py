class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr , decr = 0,0
        for i in range(1,len(nums)):
            if nums[i-1] <= nums[i] :
                incr += 1
                #print(f"{nums[i-1]} {nums[i]}")
            if nums[i-1] >= nums[i]:
                decr += 1
                #print(f"{nums[i-1]} {nums[i]}")
        #print(f"incr - {incr} decr - {decr}")
        
        if incr == len(nums)-1 or decr == len(nums)-1:
            return True
        else:
            return False