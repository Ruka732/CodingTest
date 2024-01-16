# 외판원 순회2

import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())

cost = []
for i in range(n):
  cities = list(map(int, input().split()))
  
  cost.append(cities)

def dfs(start, now, total, visited):
  global ans
  if len(visited) == n:
    if cost[now][start] != 0:
      ans = min(ans, total + cost[now][start])
    return
  
  for next in range(n):
    if cost[now][next] != 0 and next not in visited and total < ans:
      visited.append(next)
      dfs(start, next, total + cost[now][next], visited)
      visited.pop() # return 이 안되면 pop

ans = inf
for i in range(n):
  dfs(i, i, 0, [i])
print(ans)