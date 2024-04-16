# 톱니바퀴 2

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
cog = [deque(list(map(int, input().rstrip()))) for _ in range(n)]

turns = int(input())
turned = []

for _ in range(turns):
  turn = list(map(int, input().split()))
  turned.append(turn)

def left_turn(cog_idx, dir, turn_arr):
  if cog_idx == 0:
    return turn_arr
  
  if cog[cog_idx][6] != cog[cog_idx-1][2]:
    turn_arr[cog_idx-1] = -dir
    turn_arr = left_turn(cog_idx-1, -dir, turn_arr)
  
  return turn_arr

def right_turn(cog_idx, dir, turn_arr):
  if cog_idx == n-1:
    return turn_arr
  
  if cog[cog_idx][2] != cog[cog_idx+1][6]:
    turn_arr[cog_idx+1] = -dir
    turn_arr = right_turn(cog_idx+1, -dir, turn_arr)
  
  return turn_arr

for i in range(turns):
  turn_arr = [0] * n
  
  cog_idx = turned[i][0] - 1
  dir = turned[i][1]
  turn_arr[cog_idx] = dir
  
  turn_arr = right_turn(cog_idx, dir, turn_arr)
  turn_arr = left_turn(cog_idx, dir, turn_arr)
  
  for idx in range(n):
    cog[idx].rotate(turn_arr[idx])

cnt = 0

for i in range(n):
  if cog[i][0] == 1:
    cnt += 1
  else:
    continue

print(cnt)