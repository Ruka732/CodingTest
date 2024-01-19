import sys

input = sys.stdin.readline

v, e = map(int, input().split())

visited = [False] * (v + 1)
graph = [[False]*(v+1) for _ in range(v+1)]

for _ in range(e):
  n, m = map(int, input().split())
  graph[n][m] = True
  graph[m][n] = True

def dfs(v):
  global cnt
  visited[v] = True
  
  for i in range(1, v+1):
    if not visited[i] and graph[v][i]:
      dfs(i)
cnt = 0

for i in range(1, v+1):
  if not visited[i] and graph[][i]:
    cnt += 1

print(cnt)