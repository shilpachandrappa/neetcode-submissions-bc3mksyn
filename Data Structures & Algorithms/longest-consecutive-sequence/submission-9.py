class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consecutive = 0 
        
        # FIXED: Iterate over a list copy so we can safely modify num_set inside
        for num in list(num_set):
            # If 'num' was already deleted by a previous sequence sweep, skip it!
            if num not in num_set:
                continue
                
            consecutive = 1
            # Remove the starting number itself so it isn't processed again
            num_set.remove(num)
            
            # Save the original number to explore in both directions
            original_num = num
            
            # 1. Look Upwards
            while num + 1 in num_set:
                num += 1
                consecutive += 1
                num_set.remove(num)
                
            # Reset back to the start to look down
            num = original_num
            
            # 2. Look Downwards
            while num - 1 in num_set:
                num -= 1
                consecutive += 1
                num_set.remove(num)
            
            max_consecutive = max(max_consecutive, consecutive)
            
        return max_consecutive