class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += "-".join([str(ord(char)) for char in s])
            output += "_"
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        list_words = s.split("_")[:-1]
        for w in list_words:
            if w == "":
                output.append("")
            else:
                output.append("".join([chr(int(num)) for num in w.split("-")]))
        return output