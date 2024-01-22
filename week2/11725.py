# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

# 노드 개수 최대 10만 -> 탐색 한번에 100억번 들어서 메모리 터짐
# graph = [[False]*(n+1) for _ in range(n+1)]

# for i in range(n):
#   a, b = map(int, input().split())
#   graph[a][b] = True
#   graph[b][a] = True 


graph = [[] for _ in range(n+1)]
for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n+1)
visited[1] = 1
def dfs(v):
  # visited[v] == 1
  
  for i in graph[v]:
    if visited[i] == 0:
      visited[i] = v # 들르면서 자신을 호출한 부모 인덱스를 방문 배열에 기록
      # print(i)
      # print(visited)
      dfs(i)
      # return 리턴 해버리면 한 번 최대 깊이로 가고 끝내버림

dfs(1)
for i in range(2, n+1):
  print(visited[i])