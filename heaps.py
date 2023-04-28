import random

def findMedian(A, minHeap, maxHeap):
    
  if (A[-1] > heapMaximum(maxHeap)):
    maxHeapInsert(maxHeap, A[-1])
  else:
    minHeapInsert(minHeap, A[-1])

  if len(minHeap) - len(maxHeap) > 1:
    el = max(minHeap)
    minHeap.remove(el)
    maxHeapInsert(maxHeap, el)
  elif len(maxHeap) - len(minHeap) > 1:
    el = min(maxHeap)
    maxHeap.remove(el)
    minHeapInsert(minHeap, el)
  
  print(minHeap)
  print(maxHeap)
  print()
  if len(A) % 2 != 0:
    return str(maxHeap[-1])
  else:
    return f'{maxHeap[-1]} {minHeap[-1]}'
  

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

def minHeapify(A, i, N):
  p = left(i)
  q = right(i)
  if p < N and A[p] < A[i]:
    smallest = p
  else:
    smallest = i
  if q < N and A[q] < A[smallest]:
    smallest = q
  if smallest != i:
    [A[i], A[smallest]] = [A[smallest], A[i]]
    minHeapify(A, smallest, N)

def buildMaxHeap(A):
  for i in range(len(A) // 2, -1, -1):
    maxHeapify(A, i, len(A))

def buildMinHeap(A):
  for i in range(len(A) // 2, -1, -1):
    minHeapify(A, i, len(A))


def heapIncreaseKey(A, i, key):
  if key < A[i]:
    return
  A[i] = key
  while i > 0 and A[parent(i)] < A[i]:
    [A[i], A[parent(i)]] = [A[parent(i)], A[i]]
    i = parent(i)

def heapDecreaseKey(A, i, key):
  if key > A[i]:
    return
  A[i] = key
  while i > 0 and A[parent(i)] > A[i]:
    [A[i], A[parent(i)]] = [A[parent(i)], A[i]]
    i = parent(i)

def maxHeapInsert(A, key):
  A.append(float('-inf'))
  heapIncreaseKey(A, len(A) - 1, key)

def minHeapInsert(A, key):
  A.append(float('inf'))
  heapDecreaseKey(A, len(A) - 1, key)

def heapMaximum(A):
  return A[0]

def heapMinimum(A):
  return A[0]

if __name__ == "__main__":
  A = list(range(1, 11))
  random.shuffle(A)
  print(A)
  buildMaxHeap(A)
  heapIncreaseKey(A, 9, 12)
  print(A)
  maxHeapInsert(A, 11)
  print(A)
  buildMinHeap(A)
  print(A)
  minHeapInsert(A, 0)
  print(A)
