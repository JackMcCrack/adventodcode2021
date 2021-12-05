#!/usr/bin/python3

def read_input(filename):
    l = []
    lines=open(filename, "r")
    for i in lines:
        tmp = i.split()
        a = tmp[0].split(',')
        b = tmp[2].split(',')
        l.append([int(a[0]),int(a[1]),int(b[0]),int(b[1])])
    return l

def add_point(m, x, y):
    if (x,y) not in m:
        m[(x,y)] = 1 
    else:
        m[(x,y)] += 1 
    return m

if __name__ == '__main__':
    lines = {} 
    l = read_input("input")
    for i in l:
        if (i[0] == i[2]) or (i[1] == i[3]):
            # horizontal & vertical
            xc = [i[0], i[2]]
            yc = [i[1], i[3]]
            xc.sort()
            yc.sort()
            for x in range(xc[0], xc[1]+1):
                for y in range(yc[0], yc[1]+1):
                    lines = add_point(lines, x, y)
        if (abs(i[0] - i[2]) == abs(i[1] - i[3])):
            #diagonal
            if (i[0] + i[1] == i[2] + i[3]):
                # /
                if (i[0] < i[2]):
                    d = [+1,-1]
                else:
                    d = [-1,+1]
            else:
                # \
                if (i[0] < i[2]):
                    d = [+1,+1]
                else:
                    d = [-1,-1]
            c = [i[0], i[1]]
            g = [i[2], i[3]]
            lines = add_point(lines, c[0], c[1])
            while c != g:
                c = [c[0]+d[0], c[1]+d[1]]
                lines = add_point(lines, c[0], c[1])
    
    danger = 0
    for k, v in lines.items():
        if v > 1:
            danger += 1
    print(danger)
