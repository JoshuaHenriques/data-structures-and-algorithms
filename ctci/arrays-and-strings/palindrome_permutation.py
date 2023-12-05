'''
#4
Given a string, write a function to check if it is a permutation of a
palindrome. A plaindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does not
need to be limited to just dictionary words.

Examples: 
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
Input: arcecar
Output: race car
'''

# Characteristics  of a permutation of a palindrome:
# If even len(str), two of each letter
# plus a space
# If odd len(str), two of each letter and one character with odd frequency and
# that character will appear in the middle of the string
# Remove all spaces
# Time Complexity: O(N)
# Space Complexity: O(N)
def check_perm_of_pali(str: str) -> bool:
	freq = {}
	
	for char in str: # O(N)
		if char == " ":
			continue
		freq[char] = freq.get(char, 0) + 1
	odd = False
	for value in freq.values():
		if value % 2 == 1:
			if odd:
				# We have more than one char that appears an odd number of times
				return False
			odd = True
	return True

if __name__ == "__main__":
	print(check_perm_of_pali("racdtcar"))
	print(check_perm_of_pali("racdcar"))
	print(check_perm_of_pali("racar"))
	print(check_perm_of_pali("racecar"))