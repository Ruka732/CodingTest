# 탈출

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]

distance = [[0]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()

for i in range(n):
  for j in range(m):
    
    # q에 먼저 고슴도치 위치를 넣고
    if graph[i][j] == 'S':
      q.append((i, j))
    elif graph[i][j] == 'D':
      end_x, end_y = i, j

for i in range(n):
  for j in range(m):
    
    # 이 후에 물 위치를 넣음 -> 자동적으로 고슴도치 위치 bfs 이후 물 위치가 bfs
    if graph[i][j] == '*':
      q.append((i, j))

def bfs(Dx, Dy):
  while q:
    x, y = q.popleft()
    # 도달할 수 있으면
    if graph[Dx][Dy] == 'S':
      return distance[Dx][Dy]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
          graph[nx][ny] = 'S'
          distance[nx][ny] = distance[x][y] + 1
          q.append((nx, ny))
        elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
          graph[nx][ny] = '*'
          q.append((nx, ny))
  return 'KAKTUS'

print(bfs(end_x, end_y))