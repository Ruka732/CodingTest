# 신입 사원

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  
  recruit = []
  for _ in range(n):
    # recruit : 등수들임
    recruit.append(list(map(int, input().split())))
  
  cnt = 1
  recruit.sort()
  rank = recruit[0][1]
  for i in range(1, n):
    if rank > recruit[i][1]:
      rank = recruit[i][1]
      cnt += 1
  
  print(cnt)