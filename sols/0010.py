import tqdm
from math import sqrt

a = list(range(2, 2000001))

for i in tqdm.tqdm(range(2, 2000001)):
    if i != 2 and i % 2 == 0:
        a[i - 2] = False
        continue
    if i != 3 and i % 3 == 0:
        a[i - 2] = False
        continue
    if i != 5 and i % 5 == 0:
        a[i - 2] = False
        continue
    if i != 7 and i % 7 == 0:
        a[i - 2] = False
        continue
    if i != 11 and i % 11 == 0:
        a[i - 2] = False
        continue
    if i != 13 and i % 13 == 0:
        a[i - 2] = False
        continue
    for j in range(2, int(sqrt(int(i))) + 1):
        if i % j == 0:
            a[i - 2] = False
            continue

print(sum([x for x in a if x]))
