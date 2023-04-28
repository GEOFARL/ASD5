import sys
from heaps import findMedian

input_file = sys.argv[1]

with open(input_file) as f:
  A = [int(l.strip()) for l in f.readlines()][1:]

medians = []

for i in range(len(A)):
  medians.append(findMedian(A[:i+1]))
