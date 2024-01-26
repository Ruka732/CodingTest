# 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

s, end_x, end_y = map(int, input().split())

q = deque()
virus = []

for i in range(n):
  for j in range(n):
    if graph[i][j] > 0:
      virus.append((graph[i][j], i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(s, x, y):
  global virus
  q.append(virus)
  
  cnt = 0
  
  while q:
    if cnt == s:
      return
    
    for _ in range(len(q)):
      virus, x, y = q.popleft()
      
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], nx, ny))
    
    cnt += 1

  return graph[x-1][y-1]

virus.sort()

print(bfs(s, end_x, end_y))