a, b, c = map(int, input().rsplit())

print(a**b%c)
print(a**(b//2)%c)
print(a**(b//4)%c)