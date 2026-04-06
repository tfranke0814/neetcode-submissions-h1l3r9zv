class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        i, j, k = 0, 1, len(nums)-1
        while i < len(nums) - 2:
            while j != k:
                while k > j:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        res.add(tuple(triplet))
                    k-=1
                j+=1
                k=len(nums)-1
            i+=1
            j=i+1
            k=len(nums)-1
        return [list(triplet) for triplet in res]