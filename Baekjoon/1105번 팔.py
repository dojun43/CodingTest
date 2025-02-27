import sys

l,r = input().split()
cnt = 0

if len(l) != len(r):
    print(cnt)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if r[i] == '8':
                cnt += 1
        else:
            break
    print(cnt) 