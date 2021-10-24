'''
#6 Implement a method to perform basic string compression using the counts of
repeated characters. If the "compressed" string would not become smaller than
the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).

Examples: 
Input aabcccccaaa
Output a2b1c5a3
'''

from typing import List

def string_compression(string: str) -> str:
	list_str = list(string)
	char_cnt = 1
	char_cnt_list = []
	new = []

	for i in range(len(list_str)):
		while i + 1 < len(list_str) and list_str[i] == list_str[i+1]:
			char_cnt += 1
			list_str.pop(i)
		char_cnt_list.append(char_cnt)
		char_cnt = 1
	char_cnt_list = char_cnt_list[:len(list_str)]
	for i in range(len(list_str)):
		new.append(list_str[i])
		new.append(str(char_cnt_list[i]))

	if len(new) < len(string):
		return ''.join(new)
	return string

if __name__ == "__main__":
	print(string_compression("aabcccccaaa"))
	print(string_compression)