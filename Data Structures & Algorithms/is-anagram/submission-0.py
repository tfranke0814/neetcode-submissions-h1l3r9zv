class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        for ltr in s:
            try:
                s_dict[ltr] += 1
            except:
                s_dict[ltr] = 1

        for ltr in t:
            try:
                t_dict[ltr] += 1
            except:
                t_dict[ltr] = 1
        return s_dict == t_dict