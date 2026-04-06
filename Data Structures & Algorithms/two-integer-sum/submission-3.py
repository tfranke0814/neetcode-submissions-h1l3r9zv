class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for i_2, n in enumerate(nums[i+1:], start=i+1):
                if nums[i] + n == target:
                    return [i, i_2]