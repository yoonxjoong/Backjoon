cnt = int(input())

for i in range(cnt):
  data = list(map(int, input().split()))
  avg = sum(data[1:len(data)]) / (len(data) - 1)
  ret_list = [x for x in data[1:len(data)] if x > avg]
  print('%.3f' %round(len(ret_list)/data[0] * 100, 3) + '%')
 