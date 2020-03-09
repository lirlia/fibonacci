n = int(input())
N = [0]
flag = False
for i in range(n):
    if N[i] == 0:
        print(0)
        N.append(1)
        continue
    if i == 1 or i == 2:
        print(1)
        N.append(1)
        continue
    
    print(N[i - 1] + N[i])
    N.append(N[i - 1] + N[i])