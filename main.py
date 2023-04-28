import sys
from heaps import findMedian

input_file = sys.argv[1]

with open(input_file) as f:
  A = [int(l.strip()) for l in f.readlines()][1:]

minHeap = [A[1]]
maxHeap = [A[0]]

with open(f'output{input_file[5:]}', 'w') as f:
  f.write(f'{maxHeap[0]}\n{maxHeap[0]} {minHeap[0]}\n')
  for i in range(2, len(A)):
    if i != len(A) - 1:
      f.write(findMedian(A[:i+1], minHeap, maxHeap) + '\n')
    else:
      f.write(findMedian(A[:i+1], minHeap, maxHeap))
