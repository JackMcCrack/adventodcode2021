#!/usr/bin/python3

def read_input(filename):
    num = []
    lines=open(filename, "r")
    for i in lines:
        for j in i.strip().split(","):
            num.append(int(j))
    return num

if __name__ == '__main__':
    fish = []
    f = []
    fish = read_input("input")
    limit = 256
    d = 0
    for x in range(9):
        f.append(fish.count(x))
    while d < limit:
        print(d, sum(f), f)
        tmp = f[0]
        del f[0]
        f[6] += tmp
        f.append(tmp)
        d += 1

    print(sum(f))
