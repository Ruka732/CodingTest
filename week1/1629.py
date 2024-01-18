# 곱셈

import sys

input = sys.stdin.readline

# 나머지 분배 법칙
# (A * B) % p = ((A % p) * (B % p)) % p

def solution(a, b):
  if b == 1: 
    return a % c
  
  # temp = 
  
  if b % 2 == 0:
    solution(a, b//2)
  else:
    b = b - 1
  return

a, b, c = map(int, input().rsplit())

print(solution(a, b))