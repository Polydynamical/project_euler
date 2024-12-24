a = 2
while True:
    for i in range(1, 21):
        if a % i != 0:
            a += 2
            break
    else:
        break
print(a)
