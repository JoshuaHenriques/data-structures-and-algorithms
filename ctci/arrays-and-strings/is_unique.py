'''
#1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Examples: 
"abcdefgg"
"abcdefg"
'''
# Sort str, if not unique there dups will be continguously placed, compare the
# prev to curr
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def unique(str: str) -> bool:
	str = str.lower() # O(N)
	prev = ""
	arr = sorted(str)  # O(N log N)
	for char in arr: # O(N)
		if char == prev:
  			return False
		prev = char
	return True

# Convert str to a set which will remove dups. Compare str lengths
# Time Complexity: O(N)
# Space Complexity: O(N)
def unique1(str: str) -> bool:
    str = str.lower() # O(N)
    unique_str = set(str) # O(N)
    if len(unique_str) == len(str):
        return True
    else:
        return False

# Create a set and loop through str adding char to set and if it comes
# accross a dup return false
# Time Complexity: O(N)
# Space Complexity: O(N)
def unique2(str: str) -> bool:
	str = str.lower() # O(N)
	set_str = set() # O(N)
	for char in str: # O(N)
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
