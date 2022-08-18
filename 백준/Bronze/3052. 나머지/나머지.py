import sys

data = [int(sys.stdin.readline().rstrip()) for i in range(10)]
ret_set = set()
for i in range(len(data)):
  ret_set.add(data[i] % 42)
  
print(len(ret_set))