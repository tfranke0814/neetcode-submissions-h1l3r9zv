class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l, max_freq = 0, 0
        for r in range(len(s)):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1 
            reps =  (r-l+1) - max(hash_map.values())
            if reps > k:
                hash_map[s[l]] = hash_map[s[l]] - 1
                l+=1
            max_freq = max(max_freq, r-l+1)
        return max_freq
