class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mins = []
        highest = 1
        set_n = set(nums)
        for n in set_n:
            if not n-1 in set_n:
                mins.append(n)
        for n in mins:
            count = 1
            seq = n+1
            while seq in set_n:
                count += 1
                if count > highest:
                    highest = count
                seq += 1
        return highest