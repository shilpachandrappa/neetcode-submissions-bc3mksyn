class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        uniqueSet = set()
        pairCount = 0
        for num in nums :
            if num not in uniqueSet :
                uniqueSet.add(num)
            else :
                pairCount += 1
                uniqueSet.remove(num)
        return len(nums)//2 == pairCount
            