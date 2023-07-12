# def isalphanum(self, c):
#     return (ord('A') <= ord(c) <= ord('Z') or
#     ord('a') <= ord(c) <= ord('z') or
#     ord('0') <= ord(c) <= ord('9'))

def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1

    while (i <= j):
        while i < j and not s[i].isalnum():
            i += 1

        while j > i and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

def isPalindrome2(self, s: str) -> bool:
    string = ""
    
    for char in s:
        if char.isalnum():
            string += char.lower()

    return string == string[::-1]