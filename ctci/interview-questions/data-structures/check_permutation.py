'''
#2 Given two strings, write a method to decide if one is a permutation of the
other.

Examples:
str0 = "bbca"
str1 = "abbc"

Hints 
#1      
#84     
#122   
#131
'''

# If both strings aren't the same length then return false, update strings to
# lowercase, sort strings and compare them.
def permutation(str0: str, str1: str) -> bool:
	if len(str0) != len(str1): 
		return False
	str0, str1 = str0.lower(), str1.lower()
	str0, str1 = sorted(str0), sorted(str1) # O(N log N)
	return str0 == str1
	# if str0.__eq__(str1): 
	# 	return True
	# else: 
	# 	return False

# Record frequency of characters in str0 with dictionary, then run through str1
# removing str[char] from dictionary, if dictionary is 0 then its a permutation
def permutation1(str0: str, str1: str) -> bool:
	if len(str0) != len(str1): 
		return False
	count0 = {}
	for char in str0:
		count0[char] = count0.get(char, 0) + 1
	for char in str1:
		if char in count0:
			count0[char] -= 1
			if count0[char] == 0:
				del count0[char]
		else:
			return False
	return len(count0) == 0 

if __name__ == "__main__":
	str0 = "bbca"
	str1 = "bcba"
	print(f'Is str0 a permutation of str1: {permutation(str0, str1)}') 
	print(f'Is str0 a permutation of str1: {permutation1(str0, str1)}') 