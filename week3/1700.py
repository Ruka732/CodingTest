# 멀티탭 스케줄링

import sys

input = sys.stdin.readline

n, k  = map(int, input().split())

schedule = list(map(int, input().split()))

if n >= k :
  print(0)
  exit()

plug = set()
cnt = 0

def find_value(idx):
  result = 0
  max_idx = -1
  for num in plug:
    try:
      num_idx = schedule[idx:].index(num)
    except :
      num_idx = k
    if max_idx < num_idx:
      result, max_idx = num, num_idx
  
  return result

for idx, num in enumerate(schedule):
  plug.add(num)
  if len(plug) > n:
    cnt += 1
    last_used = find_value(idx)
    plug.discard(last_used)

print(cnt)