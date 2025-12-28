a = "."
b = "-."
c = "--"

s = input()
x = ""
for i in range(0, len(s), 2):
    k = s[i : i + 2]
    if k == a:
        x += "0"
    elif k == b:
        x += "1"
    elif k == c:
        x += "2"

print(int(x))
