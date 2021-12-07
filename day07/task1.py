#!/usr/bin/python3

def read_input(filename):
    num = []
    lines=open(filename, "r")
    r = -1
    for i in lines:
        for i in i.strip().split(','):
            num.append(int(i))
    return num

if __name__ == '__main__':
    n = read_input("input")
    i = min(n)
    a = max(n)
    r = {}
    for x in range(a-i+1):
        f = 0
        for m in range(len(n)):
            f += abs(x-n[m])
        print(x, f)
        r[x] = f
    minfule = 999999999
    for k,v  in r.items():
        if v <= minfule:
            minfule = v
    print(minfule)


