N, M = map(int, input().split())
lst = []

def back(cnt):
  if len(lst) == M:
    print(" ".join(map(str, lst)))
    return  
  for i in range(cnt, N+1):
    #if i not in lst:
      lst.append(i)
      back(i)
      lst.pop()

back(1)
