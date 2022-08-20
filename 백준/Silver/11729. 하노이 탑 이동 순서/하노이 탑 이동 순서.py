def hanoi(k, start, end, sub):
  if k == 1:
    print(start, end)
    return

  hanoi(k-1, start, sub, end)
  print(start, end)
  hanoi(k-1, sub, end, start)

cnt = int(input())

print((2**cnt) - 1)
hanoi(cnt, 1, 3, 2)



