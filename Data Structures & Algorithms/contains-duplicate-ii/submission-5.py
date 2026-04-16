class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums) :
            if num not in seen :
                seen[num] = i
            else :
                #print(seen[num])
                if abs(seen[num] - i) <= k:
                    return True
                else :
                    seen[num] = i
        return False

