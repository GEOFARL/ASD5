def findMedian(A, minHeap, maxHeap):

    if (A[-1] < heapMaximum(maxHeap)):
        maxHeapInsert(maxHeap, A[-1])
    else:
        minHeapInsert(minHeap, A[-1])

    if len(maxHeap) - len(minHeap) > 1:
        el = heapExtractMax(maxHeap)
        minHeapInsert(minHeap, el)
    elif len(minHeap) - len(maxHeap) > 1:
        el = heapExtractMin(minHeap)
        maxHeapInsert(maxHeap, el)

    if len(A) % 2 != 0:
        if len(maxHeap) > len(minHeap):
            return str(maxHeap[0])
        else:
            return str(minHeap[0])
    else:
        return f'{maxHeap[0]} {minHeap[0]}'


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


def heapExtractMax(A):
    if len(A) < 1:
        return
    max = A[0]
    A[0] = A[len(A) - 1]
    A.pop()
    maxHeapify(A, 0, len(A))
    return max


def heapExtractMin(A):
    if len(A) < 1:
        return
    min = A[0]
    A[0] = A[len(A) - 1]
    A.pop()
    minHeapify(A, 0, len(A))
    return min
