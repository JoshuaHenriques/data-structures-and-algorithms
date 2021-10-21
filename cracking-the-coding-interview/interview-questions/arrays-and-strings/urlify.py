'''
#3 Write a method to replace all spaces in a string with '%20'. You many assume
that the string has sufficent space at the end to hold the additional
characters, and that you are given the "true" length of the string. (Notes: If
implementing in Java, please use a character array so that you can perform this
operation in place.) 

Examples:
Input:		"Mr John Smith		", 13
Output:		"Mr%20John%20Smith"
'''

# Copy str up until the "true" length into new String, then replace every space
# to "%20" 
def urlify(str: str, length: int) -> str:
	url = ""
	for char in range(0, length): # O(N)
		if str[char] == " ":
			url += "%20"
			continue
		url += str[char]
	return url

if __name__ == "__main__":
	str0 = "Mr John Smith     "
	print(str0)
	print(urlify(str0, 13))
	
	str1 = "hi bud  "
	print(str1)
	print(urlify(str1, 6))