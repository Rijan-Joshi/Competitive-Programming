#Using zipping in python for the first time

N, Y = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(Y)]

for m in zip(*marks):
    print(sum(m)/Y)