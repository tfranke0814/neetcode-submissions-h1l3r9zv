class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        start_color = image[sr][sc]
        if start_color == color:
            return image
        image[sr][sc] = color
        if sr+1 < m and image[sr+1][sc] == start_color:
            image = self.floodFill(image, sr+1, sc, color)
        if sr-1 >= 0 and image[sr-1][sc] == start_color:
            image = self.floodFill(image, sr-1, sc, color)
        if sc+1 < n and image[sr][sc+1] == start_color:
            image = self.floodFill(image, sr, sc+1, color)
        if sc-1 >=0 and image[sr][sc-1] == start_color:
            image = self.floodFill(image, sr, sc-1, color)
        return image