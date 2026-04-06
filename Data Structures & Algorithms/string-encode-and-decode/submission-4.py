class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "Null"
        parts = []
        for s in strs:
            parts.append("-".join([str(ord(char)) for char in s]))
        return "_".join(parts)
    def decode(self, s: str) -> List[str]:
        if s == "Null":
            return []
        output = []
        encoded_words = s.split("_")
        for w in encoded_words:
            if w == "":
                output.append("")
            else:
                output.append("".join([chr(int(num)) for num in w.split("-")]))
        return output