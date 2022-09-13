a, b = input().split()

tmp = a[0]
tmp2 = a[2]
a = a.replace(a[2],'')
a = a.replace(a[0], tmp2)
a = a + tmp

tmp = b[0]
tmp2 = b[2]
b = b.replace(b[2],'')
b = b.replace(b[0], tmp2)
b = b + tmp

print(max(int(a),int(b)))