# N과 M(1)
from itertools import permutations 
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [0]
for i in range(1, n+1):
  nums.append(i)

visited = [False for _ in range(n+1)]
output_arr = []

def find_seq():
  if len(output_arr) == m:
    # print(output_arr)
    result = ' '.join(map(str, output_arr))
    print(result)
    return
  
  for idx in range(1, n+1):
    if not visited[idx]:
      current = nums[idx]
      output_arr.append(current)
      visited[idx] = True
      find_seq()
      
      output_arr.pop()
      visited[idx] = False

find_seq()