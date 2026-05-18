class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights
        expected = sorted(expected)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i] :
                count += 1
        #print(expected)
        return count