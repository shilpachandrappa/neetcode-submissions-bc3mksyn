class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(si , ti):
            if si == len(s) : return True
            if ti == len(t) : return False
            if s[si] == t[ti] :
                return rec(si+1 , ti+1)
            return rec(si , ti+1)
        return rec(0,0)