#!/usr/bin/python3

def read_input(filename):
	read = []
	lines=open(filename, "r")
	for i in lines:
		read.append(int(i.strip()))
	return read

if __name__ == '__main__':
	f = read_input("input")
	read = []
	win = []
	for i in f:
		read.append(int(i))
	l = 9999999
	count = 0
	for i, j in enumerate(read):
		if len(read) > i+2:
			win.append(read[i] + read[i+1] + read[i+2])
	for i in win:
		if i > l:
			count += 1
		#else:	
		l = i
	print(count)
