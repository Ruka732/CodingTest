# 연산자 끼워넣기

import sys

input = sys.stdin.readline

def dfs(now, total, plus, minus, multi, divide):
  if now == len(nums):
    ans.add(total)
    return ans
  
  if plus:
    dfs(now + 1, total + nums[now], plus - 1, minus, multi, divide)
    
  if minus:
    dfs(now + 1, total - nums[now], plus, minus-1, multi, divide)
    
  if multi:
    dfs(now + 1, total * nums[now], plus, minus, multi-1, divide)
    
  if divide:
    dfs(now + 1, int(total / nums[now]), plus, minus, multi, divide-1)

n = int(input())
nums = list(map(int, input().split()))
calculations = list(map(int, input().split()))
ans = set()

dfs(1, nums[0], calculations[0], calculations[1], calculations[2], calculations[3])

print(max(ans))
print(min(ans))