x = 3
left = 0 
right = x

ans = 0
while (left <= right):
    mid = (left + right) // 2 
    print("MId", mid)
    squared = mid * mid

    if (squared == x):
        print(mid)
        break
    elif (squared < x):
        left = mid + 1
    elif (squared > x):
        right = mid - 1
    
    if squared < x:
        ans = mid
print(ans)