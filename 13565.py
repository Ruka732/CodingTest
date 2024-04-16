# 침투

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(m)]
# visited = [[False for _ in range(n)] for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, matrix):
  matrix[x][y] = -1
  q = deque()
  q.append((x, y))
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < m and 0 <= ny < n:
        if matrix[nx][ny] == 0:
          q.append((nx, ny))
          matrix[nx][ny] = -1
  
  # for i in range(n):
  #   if matrix[-1][i] == -1:
  #     return "YES"
  # return "NO"

for i in range(n):
  if matrix[0][i] == 0:
    bfs(0, i, matrix)

print("YES" if -1 in matrix[-1] else "NO")