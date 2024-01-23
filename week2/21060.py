# 아침 산책

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v = int(input())

arr = [0] + list(map(int, input().strip()))

graph = [[] for _ in range(v+1)]
for _ in range(v-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0

def dfs(a):
  global cnt
  visited[a] = 1
  
  for i in graph[a]:
    if visited[i] == 0:
      if arr[i] == 1:
        cnt += 1
        
      else:
        dfs(i)
  return

for i in range(1, v+1):
  if arr[i] == 1:
    visited = [0] * (v+1)
    dfs(i)

print(cnt)