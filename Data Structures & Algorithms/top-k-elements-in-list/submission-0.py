class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        top_k_vals = sorted(hashmap.values(), reverse=True)[:k]
        return [key for key, val in hashmap.items() if val in top_k_vals]