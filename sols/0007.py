P = [2]
i = 3
while True:
    if len(P) == 10001:
        break
    for j in P:
        if i % j == 0:
           break 
    else:
        P.append(i)

    i += 1
print(P[-1])
