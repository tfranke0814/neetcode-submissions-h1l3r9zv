import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower().replace(" ", "")
        s = s.translate(str.maketrans('', '', string.punctuation))
        length = len(s)
        iters = int(length // 2)
        i, j = 0, length - 1
        while iters > 0:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            iters -= 1
        return True