
def bubbleSort(seq):
    # length of sequence
    n = len(seq)
    # passes
    # if there are n elements in sequence
    # there should be n-1 passes
    for i in range(n-1):
        # compare every adjacent pair
        for j in range(n-i-1):
            if seq[j] > seq[j+1]:
                # temp = seq[j]
                # seq[j] = seq[j+1]
                # seq[j+1] = temp
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def selectionSort(seq):
    n = len(seq)
    for i in range(n-1):
        # min: index of the minimum element
        min = i
        for j in range(i+1, n):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]
    return seq

def insertionSort(seq):
    n = len(seq)
    for i in range(1, n):
        marked = seq[i]
        j = i
        while j >= 1 and seq[j-1] > marked:
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = marked
    return seq


def partition(seq, start, end):
    pivot = seq[end]
    left = start
    right = end - 1
    while left <= right:
        while seq[left] <= pivot and left <= right:
            left += 1
        while seq[right] >= pivot and left <= right:
            right -= 1
        if left <= right:
            seq[left], seq[right] = seq[right], seq[left]
            left += 1
            right -= 1
    seq[left], seq[end] = seq[end], seq[left]
    return left

# wrapper function for a recursive function
def quickSort(seq):
    return recursiveQuickSort(seq, 0, len(seq)-1)

def recursiveQuickSort(seq, start, end):
    if start >= end: # base case
        return seq
    left = partition(seq, start, end)
    recursiveQuickSort(seq, 0, left-1)
    recursiveQuickSort(seq, left+1, end)
    return seq

def merge(s, s1, s2):
    i, j = 0, 0
    while i + j < len(s):
        if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
    return s

def mergeSort(seq):
    n = len(seq)
    if n < 2:
        return seq
    s1 = seq[:n//2]
    s2 = seq[n//2:]
    mergeSort(s1)
    mergeSort(s2)
    return merge(seq, s1, s2)

