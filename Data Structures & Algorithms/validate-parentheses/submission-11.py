class Solution:
    def isValid(self, s: str) -> bool:
        open_bracks = []
        for char in s:
            if char in ["(", "[", "{"]:
                open_bracks.append(char)
            if char in [")", "]", "}"] and len(open_bracks) == 0:
                return False

            if (char == ")" and open_bracks[-1] != "(" or 
                char == "]" and open_bracks[-1] != "[" or
                char == "}" and open_bracks[-1] != "{"
            ):
                return False
            
            if char in [")", "]", "}"]:
                open_bracks.pop()
        if len(open_bracks) != 0:
            return False
        return True