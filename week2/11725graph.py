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

print(graph)