class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        count = 0
        prefix_sum = {0:1}
        for num in nums :
            cur_sum += num
            target = cur_sum -k
            if target in prefix_sum :
                count += prefix_sum[target]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum,0)+1
        return count