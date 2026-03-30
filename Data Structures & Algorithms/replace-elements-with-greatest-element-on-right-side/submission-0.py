class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_streak = -1
        for i in range(len(arr)-1, -1,-1) :
            cur_max = max(arr[i], max_streak)
            arr[i] = max_streak
            max_streak = cur_max
        return arr