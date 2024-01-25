import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())

box = []

for _ in range(h):
  tray = []
  for _ in range(m):
    tray.append(list(map(int, input().split())))
  box.append(tray)

visited = [[[0]*n for _ in range(m)] for _ in range(h)]

print(box)
print(box[0])
print(box[0][1])

print(visited)