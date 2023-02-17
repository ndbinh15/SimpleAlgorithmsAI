# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:07:45 2021

@author: truon
"""

class Graph:
    def __init__(self, row, col, g):
        self.row = row
        self.col = col
        self.graph = g
        
    def is_safe(self, i, j, visited):
        return(i >= 0 and i < self.row and 
               j >= 0 and j < self.col and 
               not visited[i][j] and self.graph[i][j] == 1)
        
    def count(self):
        visited = [[False for j in range(self.col)] for i in range(self.row)]
        count = 0
        queue = []
        
        for r in range(self.row):
            for c in range(self.col):
                if self.is_safe(r, c, visited):
                    count += 1
                    queue.append((r, c))
                    visited[r][c] = True
                    
                    while queue:
                        x, y = queue.pop(0)
                        """
                        0 x 0
                        0 x 0
                        0 0 0
                        """
                        if(self.is_safe(x-1, y, visited)):
                            queue.append((x-1,y))
                            visited[x-1][y] = True
                        """
                        0 0 0
                        x x 0
                        0 0 0
                        """
                        if(self.is_safe(x, y-1, visited)):
                            queue.append((x,y-1))
                            visited[x][y-1] = True
                        """
                        0 0 0
                        0 x 0
                        0 x 0
                        """
                        if(self.is_safe(x+1, y, visited)):   
                            queue.append((x+1,y))
                            visited[x+1][y] = True
                        """
                        0 0 0
                        0 x x
                        0 0 0
                        """
                        if(self.is_safe(x, y+1, visited)):
                            queue.append((x,y+1))
                            visited[x][y+1] = True 
                        """
                        0 0 0
                        0 x 0
                        0 0 x
                        """
                        if(self.is_safe(x+1, y+1, visited)):
                            queue.append((x+1,y+1))
                            visited[x+1][y+1] = True
                        """
                        0 0 x
                        0 x 0
                        0 0 0
                        """
                        if(self.is_safe(x-1, y+1, visited)):
                            queue.append((x-1,y+1))
                            visited[x-1][y+1] = True
                        """
                        0 0 0
                        0 x 0
                        x 0 0
                        """
                        if(self.is_safe(x+1, y-1, visited)):
                            queue.append((x+1,y-1))
                            visited[x+1][y-1] = True
        return count 
        
if __name__ == "__main__":
    graph = [[1,0,1,0,0,0,1,1,1,1],
             [0,0,1,0,0,0,1,0,0,0],
             [1,1,1,1,0,0,1,0,0,0],
             [1,0,0,1,0,1,0,0,0,0],
             [1,1,1,1,0,0,0,1,1,1],
             [0,1,0,1,0,0,1,1,1,1],
             [0,0,0,0,0,1,1,1,0,0],
             [0,0,0,1,0,0,1,1,1,0],
             [1,0,1,0,1,0,0,1,0,0],
             [1,1,1,1,0,0,0,1,1,1]]
    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)
    print(g.count(), "islands")