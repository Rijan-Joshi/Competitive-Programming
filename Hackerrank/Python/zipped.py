#Using zipping in python for the first time

N, y = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(y)]

for m in zip(*marks):
    print(sum(m)/y)