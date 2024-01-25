n = str(input())

result = 0 
cnt = 0
a = 0
arr = []
if int(n) < 10:
  arr.append(0)
  arr.append(int(n))
else:
  arr.append(int(n[0]))
  arr.append(int(n[1]))

while a != int(n):
  result = arr[0] + arr[1]
  a = arr[1]*10 + result%10
  arr[0] = arr[1]
  arr[1] = result%10
  cnt += 1

# print(arr)
# print(a)
# print(result)
if int(n) == 0:
  print(1) # 0일땐 while문 진입을 못함
else:
  print(cnt)