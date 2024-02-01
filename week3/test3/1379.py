# 강의실 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

lectures =[]
for _ in range(n):
  room, start, end = map(int, input().split())
  heappush(lectures, (start, end, room))
print(lectures)
cnt = 0
rooms = []
current = 0
for i in range(n-1):
  if current <= lectures[i][0]:
    cnt += 1
    current = lectures[i][1]
    rooms.append(lectures[i][2])

print(cnt)
for i in rooms:
  print(i)

# GG 예제도 못만들겠음