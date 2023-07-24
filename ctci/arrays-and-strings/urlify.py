'''
#3 Write a method to replace all spaces in a string with '%20'. You many assume
that the string has sufficent space at the end to hold the additional
characters, and that you are given the "true_end" length of the string. (Notes: If
implementing in Java, please use a character array so that you can perform this
operation in place.) 

Examples:
Input:		"Mr John Smith		", 13
Output:		"Mr%20John%20Smith"
'''

from typing import List

# Copy str up until the "true_end" length into new String, then replace every space
# to "%20" 
# Time Complexity: O(N)
# Space Complexity: O(N)
def urlify(str: str, length: int) -> str:
	url = ""
	for char in range(0, length): # O(N)
		if str[char] == " ":
			url += "%20"
			continue
		url += str[char]
	return url

# Two pointer technique that shifts characters to the buffer space then replace
# the inner spaces with '%20'
# Time Complexity: O(N)
# Space Complexity: O(1)
def urlify1(str: List[str], length: int) -> str:
	end, true_end = len(str) - 1, length - 1
	while end >= 0 and true_end >= 0: # O(N)
		if str[true_end] != " ":
			str[end] = str[true_end]
			end -= 1
			true_end -= 1
		else:
			for i in reversed("%20"): 
				str[end] = i
				end -= 1
			true_end -= 1
	return ''.join(str)

if __name__ == "__main__":
	str0 = "Mr John Smith    "
	print(str0)
	print(urlify(str0, 13))
	print(urlify1(list(str0), 13))
	
	str1 = "hi bud  "
	print(str1)
	print(urlify(str1, 6))
	print(urlify1(list(str1), 6))