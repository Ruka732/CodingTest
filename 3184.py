# 양

import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

field = [list(map(str, input().rstrip())) for _ in range(r)]

# print(field)

wolf_cnt = 0
sheep_cnt = 0
for i in range(r):
  for j in range(c):
    if field[i][j] == "v":
      wolf_cnt += 1
    elif field[i][j] == "o":
      sheep_cnt += 1

visited = [[False for _ in range(c)] for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  global wolf_cnt, sheep_cnt
  q = deque()
  q.append((x, y))
  
  visited[x][y] = True
  local_sheep = 0
  local_wolf = 0
  
  if field[x][y] == 'v':
    local_wolf += 1
  elif field[x][y] == 'o':
    local_sheep += 1
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and field[nx][ny] != '#':
        if field[nx][ny] == 'o':
          local_sheep += 1
        elif field[nx][ny] == 'v':
          local_wolf += 1
        
        # print(f'nx : {nx}, ny : {ny}')
        visited[nx][ny] = True
        q.append((nx, ny))
  # print(sheep_cnt, wolf_cnt)
  # print(local_sheep, local_wolf)
  if local_sheep > local_wolf:
    wolf_cnt -= local_wolf
  elif local_wolf >= local_sheep:
    sheep_cnt -= local_sheep

for i in range(r):
  for j in range(c):
    if field[i][j] != '#' and not visited[i][j]:
      bfs(i, j)

print(sheep_cnt, wolf_cnt)