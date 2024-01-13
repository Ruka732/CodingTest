# bubble sort

import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

for i in range(len(arr)-1):
  for j in range(i + 1, len(arr)):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]

for i in arr:
  print(i)