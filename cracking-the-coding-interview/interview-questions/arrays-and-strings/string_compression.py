'''
#6 Implement a method to perform basic string compression using the counts of
repeated characters. If the "compressed" string would not become smaller than
the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).

Examples: 
Input aabcccccaaa
Output a2b1c5a3
'''

def string_compression(str: str) -> str:
	dict = {}
	comp_str = ""
	for char in str:
		dict[char] = dict.get(char, 0) + 1
	print(dict)

if __name__ == "__main__":
	string_compression("aabcccccaaa")
	print(set("aabcccccaaa"))