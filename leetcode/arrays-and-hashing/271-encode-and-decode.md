# Q271. Encode and Decode
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

*Example 1:*

```
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
```

*Example 2:*

```
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
```

## Solution

### Approach
Encode the string by putting the length of the word in front of the word with the dilimeter '#' in between them. When decoding the length of the word is used to get to the next word.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def encode(self, strs):
    string = ""

    for word in strs:
        string = str(len(word)) + "#" + word

    return string

def decode(self, str):
    array = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        array.append(str[j + 1:j + 1 + length])
        i = j + 1 + length
```