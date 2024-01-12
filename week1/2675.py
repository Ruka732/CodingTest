# 문자열 반복

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
  arr= list(map(str, input().split()))
  
  a = int(arr[0])
  
  b = list(arr[1])
  
  for i in b:
    print(a * i, end = '', sep = '')
  
  print()

