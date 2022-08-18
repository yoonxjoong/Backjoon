import sys
data = [int(sys.stdin.readline()) for i in range(9)]
ret = max(data)
print(ret)
print(data.index(ret)+1)