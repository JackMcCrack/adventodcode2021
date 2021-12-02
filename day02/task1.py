#!/usr/bin/python3

def read_input(filename):
    read = []
    lines=open(filename, "r")
    for i in lines:
        read.append(i.strip())
    return read

if __name__ == '__main__':
    f = read_input("input")
    ho = 0
    de = 0
    for l in f:
        dire = l.split(" ", 1)[0]
        dist = int(l.split(" ", 1)[1])
        if dire == "forward":
            ho += dist
        if dire == "down":
            de += dist
        if dire == "up":
            de -= dist
    print(ho, de, ho*de)
