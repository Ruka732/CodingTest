# 스타트와 링크

import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]

inf = 1e10
res = inf

def find_least(l, idx):
  global res
  if l == n//2:
    start = 0
    link = 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          start += matrix[i][j]
        elif not visited[i] and not visited[j]:
          link += matrix[i][j]
    res = min(res, abs(start - link))
    return
  
  for i in range(idx, n):
    if not visited[i]:
      visited[i] = True
      find_least(l+1, i+1)
      visited[i] = False

find_least(0,0)
print(res)