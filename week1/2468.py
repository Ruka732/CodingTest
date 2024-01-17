# 안전영역

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = []
max_num = 0

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] > max_num:
      max_num = graph[i][j] # 최대 높이 찾기

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, value, visited):
  q = deque()
  q.append((a, b))
  visited[a][b] = 1
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n: # 영역 밖으로 나가지 않게
        if graph[nx][ny] > value and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append((nx, ny))

result = 0
for i in range(max_num): # 잠기지 않는 영역 찾기
  visited = [[0] * n for _ in range(n)] # 매번 높이를 바꿀 수 있게 visited를 매번 생성
  cnt = 0
  
  # 브루트 포스
  for j in range(n):
    for k in range(n):
      if graph[j][k] > i and visited[j][k] == 0 :
        bfs(j, k, i, visited)
        cnt += 1
  
  if result < cnt:
    result = cnt

print(result)

# 직접 구현은 못할듯