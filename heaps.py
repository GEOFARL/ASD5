def findMedian(A):
  print(A)

def parent(i):
  return i // 2

def left(i):
  return 2 * i

def right(i):
  return 2 * i + 1

def maxHeapify(A, i, N):
  p = left(i)
  q = right(i)
  if p < N and A[p] > A[i]:
    largest = p
  else:
    largest = i
  if q < N and A[q] > A[largest]:
    largest = q
  if largest != i:
    [A[i], A[largest]] = [A[largest], A[i]]
    maxHeapify(A, largest, N)