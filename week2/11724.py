# 연결 요소의 개수

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(a):
  visited[a] = 1
  
  for i in graph[a]:
    if visited[i] == 0:
      dfs(i)
  
  return

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (v+1)
cnt = 0

for i in range(1, v+1):
  if visited[i] == 0:
    dfs(i)
    cnt += 1

print(cnt)
# print(graph)