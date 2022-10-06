class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        #visited = set([])
        
        to_visit = [(sr, sc)]
        m_color = image[sr][sc]
        
        if m_color == color: return image
        
        while len(to_visit) != 0:
            x,y = to_visit.pop()

            if image[x][y] == color:
                continue

            image[x][y] = color
            #visited.add((x,y))

            for (a, b) in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if a < 0 or a >= len(image): continue
                if b < 0 or b >= len(image[0]): continue
                if image[a][b] == m_color:
                    to_visit.append((a,b))

        return image
                                

        