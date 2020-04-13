#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'
frame = [0,1,2]
n = 3	
for i in range(0, len(dna)):
	j = frame*n
	print(i, j[i], dna[i])
	i+=1

"""
dna = 'ATGGCCTTT'	
frame= (0,1,2,0,1,2,0,1,2)
for i in range(0, len(dna)):
	print(i, frame[i], dna[i])
	i+=1
	
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""

