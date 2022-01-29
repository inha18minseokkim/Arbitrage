import sys
n,m = list(map(int,sys.stdin.readline().split(' ')))
arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().split()))

print(arr)
