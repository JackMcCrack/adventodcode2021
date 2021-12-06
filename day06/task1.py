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
    fish = read_input("input")
    limit = 80
    d = 0
    while d < limit:
        l = len(fish)
        for i in range(l):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
        d += 1
    print(len(fish))
