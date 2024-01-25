# 토마토

import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())

box = []

for _ in range(h):
  tray = []
  for _ in range(m):
    tray.append(list(map(int, input().split())))
  box.append(tray)

visited = [[[0]*n for _ in range(m)] for _ in range(h)]

q = deque()

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
  for j in range(m):
    for k in range(n):
      if box[i][j][k] == 1:
        q.append((i, j, k))
        visited[i][j][k] = 1

def bfs(visited):
  while q:
    z, x, y = q.popleft()
    
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n:
        if box[nz][nx][ny] == -1:
          visited[nz][nx][ny] = -1
          continue
        elif visited[nz][nx][ny] == 0 and box[nz][nx][ny] == 0:
          visited[nz][nx][ny] = visited[z][x][y] + 1
          q.append((nz, nx, ny))
  
  return visited

def find_max(graph):
  max_result = [i for sublist1 in graph for sublist2 in sublist1 for i in sublist2]
  return max(max_result)


result = bfs(visited)
# print(visited)
for i in range(h):
  for j in range(m):
    for k in range(n):
      if visited[i][j][k] == 0:
        print(-1)
        # print(visited)
        exit()

print(find_max(visited)-1)

# 약 50퍼 까지 돌았음.