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
  if len(visited) == n: # 모든 도시에 들렀다면
    if cost[now][start] != 0: # 지금 도시에서 처음 도시로 돌아갈 수 있다면
      ans = min(ans, total + cost[now][start])
    return
  
  for next in range(n):
    # 갈 수 있고, 이미 들른 도시가 아니고, 비용이 덜 든다면
    if cost[now][next] != 0 and next not in visited and total < ans:
      visited.append(next)
      dfs(start, next, total + cost[now][next], visited)
      visited.pop() # return 이 안되면 pop

ans = inf
for i in range(n):
  dfs(i, i, 0, [i])
print(ans)