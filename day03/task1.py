#!/usr/bin/python3

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    f = read_input("input")
    read = []
    for i in f:
        read.append(list(i))
    zero = [0 for x in range(len(read[0]))]
    one = [0 for x in range(len(read[0]))]
    for i in read:
        for j in range(len(i)):
            if int(i[j]) == 0:
                zero[j] += 1
            else:
                one[j] += 1
    g = []
    e = []
    for i in range(len(zero)):
        if zero[i] > one[i]:
            g.append(1)
            e.append(0)
        else:
            g.append(0)
            e.append(1)
    gs = (''.join(str(s) for s in g))
    es = (''.join(str(s) for s in e))
    print(int(gs, 2) * int(es, 2))
#    print(int(g.join()), 2) * int(e.join(), 2)
