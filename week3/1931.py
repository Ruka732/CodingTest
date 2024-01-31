# 회의실 배정

import sys

input = sys.stdin.readline

n = int(input())

meeting = []

for i in range(n):
  meeting.append(list(map(int, input().split())))

meeting.sort(key = lambda x: (x[1], x[0]))
cnt = 0

current = 0
for start, end in meeting:
  if current <= start:
    current = end
    cnt += 1

print(cnt)


# 회의 시간이 짧은 순으로 나열 ?
# 회의 시간이 빠른 순으로 나열 ?
# 회의 끝나는 시간을 순으로 나열