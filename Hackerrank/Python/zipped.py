#Using zipping in python for the first time

N, X = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(X)]

for mark in zip(*marks):
    print(sum(mark)/X)