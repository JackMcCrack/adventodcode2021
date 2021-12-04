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
    search = read
    idx = 0
    while len(search) > 1:
        next_search = []
        zero = 0
        one  = 0
        for i in range(len(search)):
            if search[i][idx] == "0":
                zero += 1
            else:
                one += 1
        print(zero, one)
        if zero > one:
            for i in range(len(search)):
                if search[i][idx] == "0":
                    next_search.append(search[i])
        else:
            for i in range(len(search)):
                if search[i][idx] == "1":
                    next_search.append(search[i])
        idx += 1
        search = next_search
    print(search)
    ox = (''.join(str(s) for s in search[0]))

    search = read
    idx = 0
    while len(search) > 1:
        next_search = []
        zero = 0
        one  = 0
        for i in range(len(search)):
            if search[i][idx] == "0":
                zero += 1
            else:
                one += 1
        print(zero, one)
        if zero <= one:
            for i in range(len(search)):
                if search[i][idx] == "0":
                    next_search.append(search[i])
        else:
            for i in range(len(search)):
                if search[i][idx] == "1":
                    next_search.append(search[i])
        idx += 1
        search = next_search
    print(search)
    co = (''.join(str(s) for s in search[0]))


    print(int(ox, 2) * int(co, 2))

