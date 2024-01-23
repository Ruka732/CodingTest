# 바이러스

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(a):
  visited[a] = 1
  
  for i in graph[a]:
    if visited[i] == 0:
      dfs(i)

  return

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (v+1)

dfs(1)
print(sum(visited)-1)