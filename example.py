import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

s, end_x, end_y = map(int, input().split())

q = deque()
virus = []

for i in range(n):
  for j in range(n):
    if graph[i][j] > 0:
      virus.append((graph[i][j], i, j))
virus.sort()
print(virus)
q.append(virus)
print(q)

que = deque((3, 4))
a, b, c = q.popleft()
print(que)
print(type(a))