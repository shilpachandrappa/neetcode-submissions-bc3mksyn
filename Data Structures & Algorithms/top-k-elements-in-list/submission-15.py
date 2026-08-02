from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return self.top_k_frequent_using_heap(nums,k)
        return self.top_k_bucket_sort(nums,k)
    
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
    
    def top_k_bucket_sort(self,nums,k):
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for key,value in count.items():
            freq[value].append(key)
        result = []
        for index in range(len(freq)-1,0,-1):
            for num in freq[index]:
                result.append(num)
                if len(result) == k:
                    return result
        return result