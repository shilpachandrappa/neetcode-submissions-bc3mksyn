class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr , decr = True, True
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] :
                incr = False
                #print(f"{nums[i-1]} {nums[i]}")
            if nums[i-1] > nums[i]:
                decr = False
                #print(f"{nums[i-1]} {nums[i]}")
        #print(f"incr - {incr} decr - {decr}")
        
        
        return incr or decr