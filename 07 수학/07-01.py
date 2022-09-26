A, B, C = map(int, input().split())
i = 0
while True:
    if B >= C:
        break
    elif A >= (C-B)*i:
        i += 1
        continue
    else:
        break
if i == 0:
    print(-1)
else:
    print(i)