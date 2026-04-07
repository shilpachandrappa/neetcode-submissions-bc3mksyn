class Solution:
    def countElements(self, arr: List[int]) -> int:
        next_elements = Counter(arr)
        #print(next_elements)
        count = 0
        for num in next_elements :
            if num+1 in next_elements:
                count += next_elements[num]
        return count