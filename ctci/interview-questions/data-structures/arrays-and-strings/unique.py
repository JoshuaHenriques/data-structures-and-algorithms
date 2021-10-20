from typing import List

'''
#1	Implement an algorithm to determine if a string has all unique characters.
	What if you cannot use additional data structures?

	Examples: 
	"abcdefgg"
	"abcdefg"

Hints
#44 	Try a hash table
#117 	Could a bit vector be useful?
#132    Can you solve it in O(N log N) time? What might a solution like that
		look like?
'''

# Sort str, if not unique there dups will be continguously placed, compare the
# prev to curr
def unique(str: str) -> bool:
	str = str.lower()
	prev = ""  # O(1)
	arr = sorted(str)  # O(N log N)
	for char in arr:
		if char == prev:
  			return False  # O(1)
		prev = char  # O(N)
	return True

# Convert str to a set which will remove dups. Compare str lengths
def unique1(str: str) -> bool:
    str = str.lower()
    unique_str = set(str)
    if len(unique_str) == len(str):
        return True
    else:
        return False

# Create a set and loop through string adding char to set and if it comes
# accross a dup return false
def unique2(str: str) -> bool:
	str = str.lower()
	set_str = set()
	for char in str:
		if char in set_str:
			return False
		set_str.add(char)
	return True


if __name__ == "__main__":
    str = "joshua"
    str1 = "joshua"
    str2 = "joshua"

    assert unique(str) == True, "This string is not unique!"
    print("String is unique")

    assert unique1(str1) == True, "This string is not unique!" 
    print("String is unique")

    assert unique2(str2) == True, "This string is not unique!"
    print("String is unique")
