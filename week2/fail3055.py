# 탈출

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(str, input().strip())))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'S':
      start = [(i, j)]
    elif graph[i][j] == 'D':
      end_i = i
      end_j = j
    elif graph[i][j] == '*':
      water = [(i, j)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


visited = [[0]*m for _ in range(n)]

def bfs(x, y):
  water_q = deque()
  water_q.append(water[0])
  
  q = deque()
  q.append(start[0])
  visited[x][y] = 0
  
  while water_q and q:
      a, b = water_q.popleft()
      x, y = q.popleft()
      
      for i in range(4):
        na = a + dx[i]
        nb = b + dy[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= na < n and 0 <= nb < m:
          if graph[na][nb] == 'D' or graph[na][nb] == 'X' or graph[na][nb] == 'S' or graph[na][nb] == '*':
            continue
          else:
            graph[na][nb] = '*'
            water_q.append((na, nb))
            # print(na, nb)
        
        if 0 <= nx < n and 0 <= ny < m:
          if graph[nx][ny] == '*' or graph[nx][ny] == 'X':
            continue
          elif graph[nx][ny] == '.':
            graph[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            print(nx, ny)
          elif graph[nx][ny] == 'D':
            return visited[x][y] + 1
  return 'KAKTUS'

print(bfs(start[0][0], start[0][1]))