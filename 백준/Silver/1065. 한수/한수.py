ret = 0
num = int(input())
for i in range(num):
  str_list = list(str(i+1))
  d = 0
  tmp_set = set()
  for p1, p2 in zip(str_list, str_list[1:]):
     tmp_set.add(int(p2)-int(p1))
  if len(tmp_set) < 2:
    ret = ret + 1
print(ret)