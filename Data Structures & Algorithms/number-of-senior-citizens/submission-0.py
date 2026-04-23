class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details :
            age = passenger[11:13]
            if int(age) > 60:
                count+=1
            #print(age)
        return count