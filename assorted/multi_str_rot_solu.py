from typing import List

# Multiple solutions involving rotating strings

# Pythonic
# Rotate string left and right an int
# Time Complexity: O(1)
# Space Complexity: O(N)
def slicing_rotate(str0: str, rot: int):
	if rot > len(str0):
		rot = rot % len(str0)

	# Slice string in two parts for left and right
	Lfirst = str0[0:rot]
	Lsecond = str0[rot:]
	Rfirst = str0[0:len(str0) - rot]
	Rsecond = str0[len(str0) - rot:]

	# Now concatenate two parts together
	print("Left Rotation: ", Lsecond + Lfirst)
	print("Right Rotation: ", Rsecond + Rfirst)
		
# Generate all rotations of a given string
# Using string concatenation
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def all_rotations(str0: str):
	# Concatenate str with itself
	concat = str0 + str0
	string = ''

	# Print all substrings of size len(str0)
	for i in range(len(str0)):
		for j in range(len(str0)):
			string += concat[i+j] 
		print(string)
		string = ''

if __name__ == "__main__": 
	slicing_rotate('jeffgoomba', 5)
	slicing_rotate('jeffgoomba', 15)
	all_rotations('jeffgoomba')