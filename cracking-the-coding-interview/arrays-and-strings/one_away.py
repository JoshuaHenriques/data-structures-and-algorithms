'''
#5
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.

Examples: 
pale,	ple		->	true
pales,	pale	->	true
pale,	bale	->	true
pale,	bake	->	false
'''
# Time Complexity: O(N)
# Space Complexity: O(N)
def one_away(str0: str, str1: str) -> bool:
	# Remove character
	if len(str0) - len(str1) == 1:
		return True
	
	# Insert character
	elif len(str0) - len(str1) == -1:
		return True
	# Same length, check if more than two characters are changed
	elif len(str0) - len(str1) == 0:
		dict = {}
		flag = False
		for i, char in enumerate(str0): # O(N)
			if str0[i] != str1[i]:
				if flag == True:
					return False
				flag = True
		return True
	else:
		return False

if __name__ == "__main__":
	print(one_away("pale", "ple"))
	print(one_away("pales", "pale"))
	print(one_away("pale", "bale"))
	print(one_away("pale", "bake"))