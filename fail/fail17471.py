# 게리맨더링

import sys
from collections import defaultdict, deque
from itertools import combinations

input = sys.stdin.readline

n = int(input())

population = list(map(int, input().split()))
linked = defaultdict(list)
edges = defaultdict(list)

for idx in range(1, n+1):
  edge = list(map(int, input().split()))
  linked[idx].append(edge[1:])
  edges[idx].append(edge[0])

# for idx in linked:
#   print(idx)
#   print(linked[idx][0])

visited = [False for _ in range(n+1)]
for i in range(1, (n//2) + 1):
  combs = combinations(n, i)

def is_linked(visited, combs):
  for i in range(len(combs)):
    for members in combs[i]:
      if not visited[members]:
        return False
  
  return True

def bfs(start):
  total = population[start]
  q = deque()
  q.append((start, total))
  
  visited[start] = True
  
  while q:
    curr_vertex, cur_popul = q.popleft()
    
    for adj_vertex in linked[curr_vertex][0]:
      if not visited[adj_vertex]:
        cur_popul += population[adj_vertex]
        q.append((adj_vertex, cur_popul))

# is_linked