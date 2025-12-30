n = int(input())

s = input()
arr = [ord(x) - ord('0') for x in s]
cnt = [arr.count(m) for m in [0,1,2]]
need = len(arr) // 3

#Pass left to right for replacing larger digit with smaller ones
#Look at each position from left to right, see if it is in surplus, deficit or balanced, replace the extra ones (which are large) with deficit ones(which are smaller)

for index, i in enumerate(arr):
    if cnt[i] > need:
        for k in range(i):
            if cnt[k] < need:
                cnt[i] -= 1
                cnt[k] += 1
                arr[index]  = k

#Right to left
#Replace smaller ones with big ones
for j in range(n-1, -1, -1):
    p = arr[j]
    if cnt[p] > need:
        for k in range(2, p, -1):
            if cnt[k] < need:
                cnt[p] -= 1
                cnt[k] += 1
                arr[j] = k

print(''.join([str(x) for x in arr]))

