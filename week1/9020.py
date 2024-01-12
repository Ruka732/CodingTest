# 골드바흐의 추측
import sys, math

def isPrime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(math.sqrt(n) + 1)):
      if n % i == 0:
        return False
    return True

# 최고의 경우 = 반씩 
# --> 반씩 나눠서 1씩 빼가면서 접근

import sys, math

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  num = int(input().rstrip())
  
  a = num//2
  b = num//2
  while a > 0:
    if isPrime(a) and isPrime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1