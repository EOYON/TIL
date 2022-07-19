N = int(input())
n = map(int, input().split())
m = int((N + 1) / 2)

print(sorted(n)[m - 1])