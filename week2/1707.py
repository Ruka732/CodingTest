# 이분 그래프

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v):
  visited[v] = 1
  
  for i in graph[v]:
    if visited[i] == 0:
      check[i] = (check[v]+1)%2 # 두가지 경우로 나누기 위해 2의 나머지 활용
      if not dfs(i): # 이미 이분그래프가 아니라면
        return False
    elif check[v] == check[i]:
      return False # 이동한 노드가 이미 같은 집합일 경우
  return True # 제대로 dfs가 돌았다면

k = int(input()) # 테스트 케이스만큼
for i in range(k):
  v, s = map(int, input().split())
  graph = [[] for _ in range(v+1)] # 매번 생성
  visited = [0] * (v+1)
  check = [0] * (v+1)
  
  for _ in range(s):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
  
  for i in range(1, v+1): # 아예 동떨어진 노드가 있을 수 있어서 
    if visited[i] == 0: # dfs가 돌고도 떨어져있다면 새로 dfs 호출
      isBipartite = dfs(i)
      if not isBipartite:
        print('NO') 
        break # 이분 그래프가 아니라고 판명나면 멈추기
  if isBipartite:
    print('YES')