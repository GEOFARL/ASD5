import sys
from heaps import findMedian

input_file = sys.argv[1]

with open(input_file) as f:
  A = [int(l.strip()) for l in f.readlines()][1:]

minHeap = [A[0]]
maxHeap = [A[1]]

with open(f'output{input_file[5:]}', 'w') as f:
  f.write(f'{minHeap[0]}\n{minHeap[0]} {maxHeap[0]}\n')
  for i in range(2, len(A)):
    f.write(findMedian(A[:i+1], minHeap, maxHeap) + '\n')
