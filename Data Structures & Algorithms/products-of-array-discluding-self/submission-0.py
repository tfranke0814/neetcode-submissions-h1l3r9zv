class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []

        tot = 1
        for n in nums:
            prefix.append(tot)
            tot *= n

        tot = 1
        for n in nums[::-1]:
            suffix.append(tot)
            tot *= n
        return [p*s for p, s in zip(prefix, suffix[::-1])]
