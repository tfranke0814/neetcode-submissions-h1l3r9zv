class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}
        l = 0
        minLen, res = len(s), ""
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        have = 0
        for r in range(len(s)):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            if sMap[s[r]] == tMap.get(s[r], 0):
                have+=1
            while have == len(tMap):
                if r - l + 1 <= minLen:
                    minLen = (r - l + 1)
                    res = s[l:r+1]
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        return res
        


            