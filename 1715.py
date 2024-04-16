# 카드 정렬하기
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
  heappush(cards, int(input()))

result = 0
while len(cards) > 1:
  a = heappop(cards)
  b = heappop(cards)
  
  sum_val = a + b
  result += sum_val
  heappush(cards, sum_val)

print(result)