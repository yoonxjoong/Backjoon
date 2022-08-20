import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set([input() for _ in range(n)])
cnt = 0
for _ in range(m):
  k = input()
  if k in a:
    cnt += 1

print(cnt)
