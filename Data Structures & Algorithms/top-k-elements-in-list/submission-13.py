from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.top_k_frequent_using_heap(nums,k)
    
    def top_k_frequent_using_heap(self,nums,k):
        freq = Counter(nums)
        heap = []
        for key,value in freq.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result