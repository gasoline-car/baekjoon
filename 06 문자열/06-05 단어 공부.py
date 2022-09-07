import sys

I = sys.stdin.readline
W = {}
for i in inp():
    U = I .upper()
    if U in W:
        W[U] += 1
    else:
        W[U] = 1

S = sorted(W.items(), key=lambda x: x[1], reverse=True)
if len(S) > 1 and S[0][1] == S[1][1]:
    print("?")
else:
    print(S[0][0])