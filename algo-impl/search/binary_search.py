# function to determine if a `target` exists in the sorted list `nums`
# or not using a binary search algorithm
def binary_search_recursion(array, target, left, right):
	if left > right:
		return -1
	mid = (right + left) // 2
	if target == array[mid]: 
		return mid
	elif target < array[mid]: 
		return binary_search_recursion(array, target, left, mid - 1)
	else: 
		return binary_search_recursion(array, target, mid + 1, right)

def binary_search_iterative(array, target):
	(left, right) = (0, len(array) - 1)
	
	#  loop till the search space is exhausted
	while left <= right:
		# find mid-value in the search space and compares it with the target
		mid = (right + left) // 2
		# overflow can happen. Use:
		# mid = left + (right - left) / 2
		# mid = right - (right - left) // 2

		# target is found
		if target == array[mid]:
			return mid

		# discard all elements in the right search space, 
		# including the middle element
		elif target < array[mid]:
			right = mid - 1

		# discard all elements in the left search space,
		# including the middle element
		else:
			left = mid + 1
	
	# `target` doesn't exist in the list
	return -1
	
if __name__ == '__main__':
	print(f'Binary Search Algorithm: ')
	
	nums0 = [2,5,6,8,9,10]

	# search space is nums[left...right]
	(left, right) = (0, len(nums0) - 1)
	target0 = 9
	print(f'recursive: {binary_search_recursion(nums0, target0, left, right)}')
	
	nums1 = [1,4,5,8,9]
	target1 = 9
	print(f'iterative: {binary_search_iterative(nums1, target1)}')