import random

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

def buildMaxHeap(A):
  for i in range(len(A) // 2, -1, -1):
    maxHeapify(A, i, len(A))


def heapIncreaseKey(A, i, key):
  if key < A[i]:
    return
  A[i] = key
  while i > 0 and A[parent(i)] < A[i]:
    [A[i], A[parent(i)]] = [A[parent(i)], A[i]]
    i = parent(i)

def maxHeapInsert(A, key):
  A.append(float('-inf'))
  heapIncreaseKey(A, len(A) - 1, key)


if __name__ == "__main__":
  A = list(range(1, 11))
  random.shuffle(A)
  print(A)
  buildMaxHeap(A)
  heapIncreaseKey(A, 9, 12)
  print(A)
  maxHeapInsert(A, 11)
  print(A)
