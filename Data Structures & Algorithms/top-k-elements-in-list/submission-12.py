from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        res=[]
        for item, _ in num_count.most_common(k) :
            res.append(item)
        return res
            