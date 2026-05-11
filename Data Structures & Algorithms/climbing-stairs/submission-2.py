import math
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        if n % 2 == 1:
            for i in range(0, int((n+1) / 2)):
                res += math.factorial(int(n-i)) / (math.factorial(int(n-2*i)) * math.factorial(i))
        elif n % 2 == 0:
            for i in range(0, int((n+2) / 2)):
                res += math.factorial(int(n-i)) / (math.factorial(int(n-2*i)) * math.factorial(i))
        return int(res)