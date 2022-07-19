T = int(input())

for i in range(1, T + 1):
    w = input()
    if w == w[::-1]:
        a = 1
    else:
        a = 0
    print(f"#{i} {a}" )