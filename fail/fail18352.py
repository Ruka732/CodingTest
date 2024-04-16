# 특정 거리의 도시 찾기

import sys
from collections import defaultdict, deque
from math import inf

input = sys.stdin.readline

n, m, distance, start_node = map(int, input().split())
city = defaultdict(list)

for _ in range(m):
  start, end = map(int, input().split(' '))
  city[start].append(end)

def bfs(start, cities, city, edges):
  cnt = 0
  q = deque()
  q.append(start)
  
  cnts = [inf] * (cities+1)
  visited = [False] * (cities+1)
  visited[start] = True
  
  arrive = set()
  
  while q:
    current = q.popleft()
    cnt += 1
    
    for adj in city[current]:
      if not visited[adj]:
        visited[adj] = True
        q.append(adj)
        # print(f'adj : {adj}, cnt : {cnt}')
        cnts[adj] = min(cnts[adj], cnt)
        
      # print(f'2 ! adj : {adj}, cnt : {cnt}')
      if cnts[adj] == edges:
        arrive.add(adj)
  
  return arrive

arrive = bfs(start_node, n, city, distance)
arrive = list(arrive)
arrive.sort()

if len(arrive) == 0:
  print(-1)
else:
  for members in arrive:
    print(members)