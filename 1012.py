# 유기농 배추

import sys
from collections import deque

input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(m, n, x, y, matrix, visited):
  global cnt
  
  visited[x][y] = True
  q = deque()
  q.append((x, y))
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < m and 0<= ny < n:
        if matrix[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx, ny))
  cnt += 1
  return

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())

  matrix = [[0 for _ in range(n)] for _ in range(m)]
  visited = [[False for _ in range(n)] for _ in range(m)]
  cnt = 0
  for _ in range(k):
    x, y = map(int, input().split())
    matrix[x][y] = 1
  
  for x in range(m):
    for y in range(n):
      if not visited[x][y] and matrix[x][y] == 1:
        bfs(m, n, x, y, matrix, visited)
  
  print(cnt)