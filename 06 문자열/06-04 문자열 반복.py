while True:
    case= input().split()
    R = int(case[0])
    if len(case) == 1:
        pass
    else:
        P = case[1]
        for i in range(len(P)):
            print(P[i] * R, end="")
        print()