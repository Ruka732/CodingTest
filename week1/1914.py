# 하노이의 탑

def hanoi(n, start, second, desti):
  if n == 1:
    print(start, desti)
    return
  
  hanoi(n-1, start, desti, second)
  print(start, desti)
  hanoi(n-1, second, start, desti)

n = int(input())

print(2**n - 1)

if n <= 20:
  hanoi(n, 1, 2, 3)