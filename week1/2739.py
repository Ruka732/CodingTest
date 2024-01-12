# 구구단

import sys

input = sys.stdin.readline 

n = int(input())

for i in range(1, 10):
  a = n * i
  print(f"{n} * {i} = {a}")