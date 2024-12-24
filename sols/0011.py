data = [[int(x) for x in open("../data/0011.txt").readlines()[i].split("\n")[0].split(" ")] for i in range(len(open("../data/0011.txt").readlines()))]
_max = -1

# across rows
for ri in range(20):
    for rii in range(20 - 4 + 1):
        _max = max(_max, data[ri][rii] * data[ri][rii+1] * data[ri][rii+2] * data[ri][rii + 3])
# across columns
for ci in range(20):
    for cii in range(20 - 4 + 1):
        _max = max(_max, data[cii][ci] * data[cii + 1][ci] * data[cii + 2][ci] * data[cii + 3][ci])
# diagonals
for di in range(20 - 4 + 1):
    for dii in range(20 - 4 + 1):
        _max = max(_max, data[di][dii] * data[di + 1][dii + 1] * data[di + 2][dii + 2] * data[di + 3][dii + 3])

for di in range(20 - 1, 2, -1):
    for dii in range(20 - 1, 2, -1):
        _max = max(_max, data[di][dii] * data[di - 1][dii - 1] * data[di - 2][dii - 2] * data[di - 3][dii - 3])

print(_max)
