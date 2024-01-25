# 바닥 장식

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
  badak = list(map(str, input().strip()))
  graph.append(badak)

visited = [[False]*m for _ in range(n)]
cnt = 0

def dfs(x, y):
  visited[x][y] = True
  
  if graph[x][y] == '-':
    if y+1 < m and graph[x][y+1] == '-' and not visited[x][y+1]:
      dfs(x, y+1)
    else:
      return
  elif graph[x][y] == '|':
    if x+1 < n and graph[x+1][y] == '|' and not visited[x+1][y]:
      dfs(x+1, y)
    else:
      return

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      dfs(i, j)
      cnt += 1
print(cnt)