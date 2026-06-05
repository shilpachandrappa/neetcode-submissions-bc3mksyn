class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_consecutive = 0
        
        print(nums)
        for i in range(len(nums)) :
            if nums[i-1] != nums[i] -1 :
                consecutive =1
                while i+1 <len(nums) and (nums[i+1] == nums[i]+1 or nums[i+1] == nums[i]) :
                    if nums[i+1] != nums[i] :
                        consecutive += 1
                    i+=1
                max_consecutive = max(consecutive, max_consecutive)
            
        return max_consecutive