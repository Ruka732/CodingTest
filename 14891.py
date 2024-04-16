# 톱니바퀴

import sys
from collections import deque

input = sys.stdin.readline

cogwheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

turns = int(input())
turned = []

for _ in range(turns):
  turn = list(map(int, input().split()))
  turned.append(turn)

# print(type(cogwheels[0][0]))
# print(cogwheels[0][0])

def left_turn(cog_idx, dir, turn_arr):
  if cog_idx == 0:
    return turn_arr
  
  if cogwheels[cog_idx][6] != cogwheels[cog_idx-1][2]:
    turn_arr[cog_idx-1] = -dir
    turn_arr = left_turn(cog_idx-1, -dir, turn_arr)
  # else:
  #   return turn_arr
  return turn_arr

def right_turn(cog_idx, dir, turn_arr):
  if cog_idx == 3:
    return turn_arr
  
  if cogwheels[cog_idx][2] != cogwheels[cog_idx+1][6]:
    turn_arr[cog_idx+1] = -dir
    turn_arr = right_turn(cog_idx+1, -dir, turn_arr)
  # else:
  #   return turn_arr

  return turn_arr

for i in range(turns):
  turn_arr = [0] * 4
  
  cog_idx = turned[i][0] -1
  dir = turned[i][1]
  turn_arr[cog_idx] = dir
  # print(turn_arr)
  turn_arr = right_turn(cog_idx, dir, turn_arr)
  turn_arr = left_turn(cog_idx, dir, turn_arr)
  # print(turn_arr)
  
  for idx in range(4):
    cogwheels[idx].rotate(turn_arr[idx])

  # for x in cogwheels:
  #   print(x)
# for i in range(4):
#   print(cogwheels[i])


# print(turn_arr)

score = 0
if cogwheels[0][0] == 1:
  score += 1

if cogwheels[1][0] == 1:
  score += 2

if cogwheels[2][0] == 1:
  score += 4

if cogwheels[3][0] == 1:
  score += 8

print(score)