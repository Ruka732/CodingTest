# 최댓값

arr = []

for i in range(9):
  n = int(input())
  arr.append(n)

m_num = max(arr)

print(m_num)
print(arr.index(m_num) + 1)