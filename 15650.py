# N과 M(2)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [0]
for i in range(1, n+1):
  nums.append(i)

visited = [False for _ in range(n+1)]
output_arr = []
curr_arr = []

def find_seq():
  if len(curr_arr) == m:
    output_arr = curr_arr.copy()
    print(' '.join(map(str, output_arr)))
    return
  
  for idx in range(1, n+1):
    if not visited[idx]:
      
      if len(curr_arr) > 0 and idx < curr_arr[-1]:
        continue
      
      current = nums[idx]
      visited[idx] = True
      curr_arr.append(current)
      find_seq()
      
      curr_arr.pop()
      visited[idx] = False

find_seq()