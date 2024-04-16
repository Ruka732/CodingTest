# N과 M (5)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

output_arr = []
visited = [False for _ in range(n)]

def find_seq():
  if len(output_arr) == m:
    print(' '.join(map(str, output_arr)))
    return
  
  for idx in range(n):
    if visited[idx]:
      continue
    
    current = nums[idx]
    visited[idx] = True
    output_arr.append(current)
    
    find_seq()
    
    visited[idx] = False
    output_arr.pop()

find_seq()