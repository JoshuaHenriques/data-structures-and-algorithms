'''
#9
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 using only one call to isSubstring

Example:
"waterbottle" is a rotation of "erbottlewat"
'''

# All rotations of A are contained in A+A. Thus, we can simply check whether B 
# is a substring of A+A. We also need to check A.length == B.length, otherwise 
# we will fail cases like A = "a", B = "aa"
# Time Complexity: O(1)
# Space Complexity: O(1)
def is_substring(str0: str, str1: str) -> bool:
	return str0 in str1+str1

if __name__ == "__main__":
	print(is_substring("waterbottle", "erbottlewat"))