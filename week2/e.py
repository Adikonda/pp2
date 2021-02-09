a,b = map(int, input().split())
k = (b-1) // a + 1
n = (b - 1) % a + 1
print(k, n)
