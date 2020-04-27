#!/usr/bin/env python3
# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

from math import sqrt
import fileinput

min = 0
max = 0
sum = 0
count = 0
mean = 0
sum_sqr = 0
std = 0
median = 0
data = []
for line in fileinput.input():
	count += 1
	data.append(float(line))
	sum += float(line)
	if min > float(line): 
		min = float(line)
	if max <= float(line): 
		max = float(line)
	mean = sum/count
for line in fileinput.input():
	sum_sqr += (float(line) - mean) * (float(line) - mean)
std = sqrt(sum_sqr/count)
data.sort()
if (count + 1)/2 == 0:
	median = data[int((count + 1)/2)]
else:
	median = (data[int(count/2)] + data[int(1 + count/2)])/2
	
print(f'Count: {count}')
print(f'Min: {min}')
print(f'Max: {max}')
print(f'Mean: {mean}')
print(f'Std. dev: {std}')
print(f'Median: {median}')

"""	
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
