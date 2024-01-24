# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
  distances = [int(1e9)] * (n+1)
  distances[start] = 0
  q = []
  heapq.heappush(q, [distances[start], start])
  
  while q:
    dist, node = heapq.heappop(q)
    
    if distances[node] < dist:
      continue
    
    for next_node, next_dist in graph[node]:
      distance = dist + next_dist
      if distance < distances[next_node]:
        distances[next_node] = distance
        heapq.heappush(q, [distance, next_node])
  
  return distances

dist_start = dijkstra(start)
print(dist_start[end])