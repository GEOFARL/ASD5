import sys
from heaps import findMedian

input_file = sys.argv[1]

with open(input_file) as f:
  A = [int(l.strip()) for l in f.readlines()][1:]

medians = []
minHeap = [A[0]]
maxHeap = [A[1]]

for i in range(2, len(A)):
  medians.append(findMedian(A[:i+1], minHeap, maxHeap))
