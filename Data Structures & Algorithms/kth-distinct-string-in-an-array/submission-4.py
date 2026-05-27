class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        dist_count = 0
        for str in counts :
            if counts[str] == 1 :
                dist_count += 1
                if dist_count == k :
                    return str
        return ""
