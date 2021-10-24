'''
#7
Given an image represented by an NxN matrix, where each pixel inthe image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?

Example:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]
[5,6,7,8]

[5,9,5,1]
[6,2,6,2]
[7,3,7,3]
[8,4,8,4]
'''

from typing import List

# Time Complexity: O(N^2)
# Space Complexity: O(1)
def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
	# Transpose the Matrix
	for i in range(len(matrix) - 1):
		for j in range(i + 1, len(matrix)): # O(N^2)
			# Switch the row and column indices
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	# Reverse every row
	for k in range(len(matrix)):
		for l in range(len(matrix[k]) // 2): # O(N log N)
			# opposite is the opposing index to i
			opposite = len(matrix[k]) - 1 - l
			matrix[k][l], matrix[k][opposite] = matrix[k][opposite], matrix[k][l]
	return matrix

if __name__ == "__main__":
	matrix = [[1,2,3,4],[5,6,7,8],[9,2,3,4],[5,6,7,8]]
	print(matrix)
	print(rotate_matrix(matrix))
	