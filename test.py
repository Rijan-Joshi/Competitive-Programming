x = 1001
for i in range(int(x)):
    if i * i == x:
        print(i)
        break

ans = 0
for i in range(int(x)):
    if (i * i) <= x :
        ans = i
        
print(ans)