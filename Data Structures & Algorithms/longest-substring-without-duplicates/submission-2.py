class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCnt = 0
        sub = ""
        for c in s:
            if c not in sub:
                sub += c
            elif c in sub:
                sub = sub[sub.index(c) + 1:] + c
            maxCnt = max(maxCnt, len(sub))
        return maxCnt