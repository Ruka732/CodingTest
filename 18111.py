# 마인크래프트

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

time = [0 for _ in range(257)]
height = 0

for target_h in range(257):
  blocks = b
  
  for row in range(n):
    for current_h in ground[row]:
      if current_h <= target_h:
        time[target_h] += target_h - current_h
        blocks -= target_h - current_h
      else:
        time[target_h] += 2 * (current_h - target_h)
        blocks += current_h - target_h
    
  if blocks >= 0 and time[target_h] <= time[height]:
    height = target_h

print(time[height], height)