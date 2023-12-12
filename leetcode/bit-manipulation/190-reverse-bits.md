# 190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

*Example 1:*

```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

*Example 2:*

```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

*Constraints:*

```
The input must be a binary string of length 32
```

## Optimized Solution

### Approach
For each bit in a 32 bit number we get the bit we want by shifting it by i and & by 1. Then we want to place that bit in reverse order in the res number by 'or' by that bit shifted to the left 31 - i

### Complexity
$$Time: O(1)$$

$$Space: O(1)$$

### Code
```py
def reverseBits(self, n: int) -> int:
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    
    return res
```
