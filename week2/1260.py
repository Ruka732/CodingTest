import sys
from collections import deque

input = sys.stdin.readline

def dfs(v):
  visited_dfs[v] = True
  
  print(v, end=' ')
  
  for i in range(1, a+1):
    if not visited_dfs[i] and graph[v][i]:
      dfs(i)


def bfs(v):
  visited_bfs[v] = True
  q = deque([v])
  
  while q:
    v = q.popleft()
    print(v, end=' ')
    
    for i in range(1, a+1):
      if not visited_bfs[i] and graph[v][i]:
        q.append(i)
        visited_bfs[i] = True

a, b, c = map(int, input().split())
graph = [[False]*(a+1) for _ in range(a+1)]

for _ in range(b):
  n, m = map(int, input().split())
  graph[n][m] = True
  graph[m][n] = True

visited_dfs = [False] * (a+1)
visited_bfs = [False] * (a+1)

dfs(c)
print()
bfs(c)
# 문제 인덱스는 1부터 시작해서 인덱스 꼬임 - 인덱스 1씩 늘려서 맞춰줌
# 인풋이 노드가 아닌 간선이라서 문제 - 그래프 다시 그림