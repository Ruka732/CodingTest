# 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, visited, row_size, col_size):
  moves = [[1, 0], [1, -1], [1, 1], [0, 1], [0, -1], [-1, -1], [-1, 1], [-1, 0]]
  
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      
      if 0 <= nx < row_size and 0 <= ny < col_size and not visited[nx][ny]:
        if matrix[nx][ny] != 0:
          visited[nx][ny] = True
          q.append((nx, ny))
  
  return visited

arr_cnt = []

while True:
  col_size, row_size = map(int, input().split())
  
  if col_size == 0 and row_size == 0:
    break
  
  visited = [[False for _ in range(col_size)] for _ in range(row_size)]
  
  matrix = [list(map(int, input().split())) for _ in range(row_size)]
  cnt = 0
  
  for row in range(row_size):
    for col in range(col_size):
      if matrix[row][col] != 0 and not visited[row][col]:
        # print(f'prev cnt : {cnt}')
        # print(f'cur_row : {row}, cur_col : {col}')
        visited = bfs(row, col, visited, row_size, col_size)
        # for k in visited:
        #   print(k)
        # print('---')
        cnt += 1
        # print(f'now cnt : {cnt}')
  
  arr_cnt.append(cnt)

for c in arr_cnt:
  print(c)