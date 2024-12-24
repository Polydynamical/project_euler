a = []
for i in range(1000):
    if i % 3 == 0 and i % 5 == 0:
        a.append(i)
        continue
    elif i % 3 == 0:
        a.append(i)
    elif i % 5 == 0:
        a.append(i)
    else:
        continue

print(sum(a)) 
