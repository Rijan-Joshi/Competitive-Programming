#Sorting Athlete - Medium

N, M = map(int, input().split())
datae = [list(map(int,input().split())) for _ in range(N)]
K = int(input())
sorted_data = sorted(datae, key = lambda x:x[K])

for data in sorted_data:
    print(*data)