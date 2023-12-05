'''
#8
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0

Hints: #17, #74, #102

Example:
[1,2,3,4]
[5,6,7,8]
[9,2,0,4]
[5,6,7,8]

[1,2,0,4]
[5,6,0,8]
[0,0,0,0]
[5,6,0,8]
'''

from typing import List

# Time Complexity: O(N*M)
# Space Complexity: O(N)
def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
	pairs = []
	# Traverse matrix and store indicies of '0's
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				pairs.append((i, j))
	# Loop through indicies and assign 0's to the rows and cols
	for i, j in pairs:
		for k in range(len(matrix[i])):
			matrix[i][k] = 0
			matrix[k][j] = 0
	return matrix
				

if __name__ == "__main__":
	matrix = [[1,2,3,4],[5,6,7,8],[9,0,3,4],[5,6,7,8]]
	print(matrix)
	print(zero_matrix(matrix))