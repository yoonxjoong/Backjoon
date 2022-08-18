cnt = int(input())

for j in range(cnt):
  data = input()
  ret = 0
  tmp = 0
  for i in range(len(data)):
    if data[i] == 'O':
      #print("O : " + data[i])
      tmp += 1
      #print(tmp)
    elif data[i] == 'X':
      #print("X : " + data[i])
      tmp = 0
    ret = ret + tmp
  print(ret)