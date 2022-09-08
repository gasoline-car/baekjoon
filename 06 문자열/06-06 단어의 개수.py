T = list(input())
ans = 0
while True:
    if T[0] == ' ':
        del T[0]
    if T[-1] == ' ':
        del T[-1]
    if T[0] != ' ' and T[-1] != ' ':
        break
for i in T:
    if i == ' ':
        ans += 1
print(ans+1)