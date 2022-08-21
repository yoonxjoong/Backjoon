b = list()
my_dict = dict()

m = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    if my_dict.get(a[i]):
      value = my_dict.get(a[i])
      my_dict[a[i]] = value + 1
    else:
      my_dict[a[i]] = 1

n = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
  if my_dict.get(b[i]):
    print(my_dict.get(b[i]), end=' ')
  else:
    print(0, end=' ')
