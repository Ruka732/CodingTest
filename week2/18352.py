# 특정 거리의 도시 찾기

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, cost):
  q = deque()
  q.append((x, cost)) # 시작 노드, cost
  visited[x] = 1
  result = set()
  while q:
    now, now_cost = q.popleft()
    
    for i in graph[now]:
      if visited[i] == 0:
        visited[i] = 1
        now_cost += 1
        q.append((i, now_cost))
        if q[0][1] == k:
          result.add(i)
          
  return result

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  # directed graph 이므로 단방향만
  graph[a].append(b)

visited = [0] * (n+1)

result = list(bfs(x, 0))
result.sort()
if not result:
  print(-1)
else:
  for i in result:
    print(i)