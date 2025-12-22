n = int(input())

x = y = z = 0
for i in range(n):
    a, b, c = map(int, input().split(" "))
    x += a
    y += b
    z += c

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
