import sys

input = sys.stdin.readline

n = int(input())

result = 0

def check(visitied, depth):
  global result 
  for number in range(n):
    if number in visitied:
      continue
    if find_queen(visitied, depth, number):
      if depth == n-1 :
        result+=1
      else:
        visitied[depth] = number
        check(visitied, depth+1)
        visitied[depth] = -1
        
def find_queen(visitied, depth, queen_row): 
  for v in range(depth):
    if abs(visitied[v] - queen_row) == abs(v - depth):
      return False
  return True       


for i in range(n):
  visitied = [-1 for _ in range(n)]
  visitied[0] = i
  check(visitied, 1)

if n == 1:
  result = 1
  
print(result) 