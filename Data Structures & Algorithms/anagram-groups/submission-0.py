class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            map_val = hashmap.get(sorted_str, None)
            if map_val is not None:
                map_val.append(s)
                hashmap[sorted_str] = map_val
            else:
                hashmap[sorted_str] = [s]
        return list(hashmap.values())