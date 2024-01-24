# 미로 탐색

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  q.append((x, y))
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
  return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
  arr = list(map(int, input().strip()))
  # append 쓸 경우 리스트 안에 리스트가 생성됨 -> 인덱스 오류 발생
  graph.append(arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs(0, 0))