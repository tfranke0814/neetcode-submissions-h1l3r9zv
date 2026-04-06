class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        itermap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in itermap:
                return [itermap[diff], i]
            else: 
                itermap[n] = i