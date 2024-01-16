# 나무 자르기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
  total = 0
  h = (start + end) // 2
  
  for i in arr:
    if i > h:
      total += i - h
  
  # 이진탐색
  if total < m:
    end = h - 1
  else:
    result = h
    start = h + 1

print(result)

# 자를 높이 h를 찾기위해 이진탐색 실행