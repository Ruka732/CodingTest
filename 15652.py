# N과 M (4)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [0]
for i in range(1, n+1):
  nums.append(i)

output_arr = []

def find_seq():
  if len(output_arr) == m:
    print(' '.join(map(str, output_arr)))
    return
  
  for idx in range(1, n+1):
    
    if len(output_arr) > 0 and idx < output_arr[-1]:
      continue
    
    output_arr.append(idx)
    find_seq()
    output_arr.pop()

find_seq()