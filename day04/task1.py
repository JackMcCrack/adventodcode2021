#!/usr/bin/python3

def read_input(filename):
    num = []
    crd = []
    tmp = []
    lines=open(filename, "r")
    r = -1
    for i in lines:
        if r == -1:
            num = [int(j) for j in (i.strip().split(','))]
        else:
            for i in i.strip().split():
                tmp.append(int(i))
            if r == 6:
                crd.append(tmp)
                tmp = []
                r = 0
        r += 1
    crd.append(tmp)
    return num, crd

if __name__ == '__main__':
    n, c = read_input("input")
    bing = False
    while not bing and len(n) > 0:
        i = n[0]
        n = n[1:len(n)-1]
        print('call: ', i)
        for j in range(len(c)):
            print(c[j])
            c[j] = [x if (x != i) else -1 for x in c[j]] # replace with -1 if the number got picked
            for off in range(5):
                # check horizontal and vertical
                if sum(c[j][0+off*5:5+off*5]) == -5 or c[j][0+off]+c[j][5+off]+c[j][10+off]+c[j][15+off]+c[j][20+off] == -5:
                    bing = True
            if bing:
                print('BING ', j, i, )
                for o in range(5):
                    print(c[j][0+o*5:5+o*5])
                s = sum( [ x if (x >= 0) else 0 for x in c[j] ])
                print(s, i, i*s)
                break
