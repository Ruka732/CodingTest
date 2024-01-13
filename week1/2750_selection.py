# selection sort

import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

for i in range(len(arr)):
  # 최솟값 인덱스
  min_index = i
  
  for j in range(i + 1, len(arr)):
    if arr[min_index] > arr[j]:
      min_index = j
  
  # 자리바꾸기
  arr[i], arr[min_index] = arr[min_index], arr[i]

for i in arr:
  print(i)