# 센서

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

if m >= n:
  print(0)
  sys.exit()

distance = []
for i in range(1, n):
  distance.append(sensors[i] - sensors[i-1])

distance.sort()

for _ in range(m-1):
  distance.pop()

print(sum(distance))

# 집중국당 덩어리 나눠주기
# input : 1 6 9 3 6 7
# 거리 가장 먼 3인 (1, 3) 과 (6, 6, 7, 9) 로 나눠줌
# 최종 집중국 위치 : 2, 6