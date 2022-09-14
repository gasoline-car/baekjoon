a=input()
count=0
for hi in a:
    if hi== 'A' or 'B' or 'C':
        count+=3
    elif hi== 'D' or 'E' or 'F':
        count+=4
    elif hi== 'G' or 'H' or 'I':
        count+=5
    elif hi== 'J' or 'K' or 'L':
        count+=6
    elif hi== 'M' or 'N' or 'O':
        count+=7
    elif hi== 'P' or 'Q' or 'R' or 'S':
        count+=8
    elif hi== 'T' or 'U' or 'V':
        count+=9
    elif hi== 'W' or 'X' or 'Y' or 'Z':
        count+=10
print(count)