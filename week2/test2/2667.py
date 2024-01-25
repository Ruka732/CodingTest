# 단지번호 붙이기

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*n for _ in range(n)]

q = deque()
cnt = 0

def bfs(x, y):
  global cnt
  
  q.append((x, y))
  house = 0
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    house += 1
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 1 and not visited[nx][ny]:
          graph[nx][ny] = graph[x][y] + 1
          visited[nx][ny] = True
          # house += 1
          q.append((nx, ny))
  return house

result = []
for i in range(n):
  for j in range(n):
    # houses = bfs(i, j)
    if graph[i][j] == 1 and not visited[i][j]:
      houses = bfs(i, j)
      result.append(houses)
result.sort()


print(len(result))
for i in result:
  print(i)