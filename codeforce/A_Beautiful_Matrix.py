import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = [int(data[index + i]) for i in range(n)]
    index += n
    
    if a[0] > a[1] or a[n-1] > a[n-2]:
        print("YES")
    else:
        print("NO")