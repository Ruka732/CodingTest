# 팩토리얼

import sys

input = sys.stdin.readline

n = int(input())

def fact(a):
  if a == 0:
    return 1
  else:
    return a * fact(a - 1)

print(fact(n))