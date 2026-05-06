class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        goodpair = 0
        for i, num in enumerate(nums) :
            if num in seen :
                goodpair += seen[num]
            
            seen[num] = seen.get(num,0) +1
        
        return goodpair
