# 미로 만들기

import sys
import heapq

input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
  arr = list(map(int, input().strip()))
  graph.append(arr)

visited = [[0]*n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra(x, y):
  q = []
  heapq.heappush(q, [0, 0, 0])
  visited[0][0] = 1
  
  while q:
    cost, x, y = heapq.heappop(q)
    if x == n - 1 and y == n - 1:
      print(cost)
      return
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        if graph[nx][ny] == 0:
          heapq.heappush(q, [cost + 1, nx, ny])
        else:
          heapq.heappush(q, [cost, nx, ny])

dijkstra(0, 0)