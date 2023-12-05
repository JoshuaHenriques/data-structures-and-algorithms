# def swap(A, i, j):
# 	temp = A[i]
# 	A[i] = A[j]
# 	A[j] = temp

from typing import List


def swap(A: List[int], i: int, j: int):
	A[i], A[j] = A[j], A[i]

# partition using the Lumuto partition scheme
def partition(A: List[int], l: int, r: int) -> int:
	# pick the rightmost element as a pivot from the list
	pivot = A[r]

	# elements less than the pivot will be pushed to the left of pivot_index
	# elements more than the pivot will be pushed to the right of pivot_index
	# equal elements can go either way
	pivot_index = l

	# each time we find an element less than or equal to the pivot, pivot_index
	# is incremented, and that element would be placed before the pivot
	for i in range(l, r):
		if A[i] <= pivot:
			swap(A, i, pivot_index)
			pivot_index += 1

	# swap pivot_index with pivot
	swap(A, r, pivot_index)

	# return pivot_index
	return pivot_index

def quicksort(A: List[int], l: int, r: int):
	# base case
	if l >= r: return

	# rearrange elements across pivot
	pivot = partition(A, l, r)

	# recur on sublist containing elements less than the pivot
	quicksort(A, l, pivot - 1)

	# recur on sublist containing elements more than the pivot
	quicksort(A, pivot + 1, r)


if __name__ == '__main__':
 
    A = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    quicksort(A, 0, len(A) - 1)
 
    # print the sorted list
    print(A)