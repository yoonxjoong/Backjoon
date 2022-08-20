a = set()
b = list()

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
  if b[i] in a:
    print(1, end=' ')
  else:
    print(0, end=' ')
