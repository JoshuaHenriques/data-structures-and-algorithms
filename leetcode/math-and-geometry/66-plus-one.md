# 66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

*Example 1:*

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

*Example 2:*

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

*Example 3:*

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

*Constraints:*

* 1 <= digits.length <= 100
* 0 <= digits[i] <= 9
* digits does not contain any leading 0's.


## Solution

### Approach
Reverse the list, have a variable for the carry. Iterate through the list, if there is a 9 set it to 0 and the one variable will carry it to the next number. If it wasn't a 9 we just add 1, set the carry one to 0. If we reached the end of the list and the carry is still set then we append another digit to the list. Reverse the list again and return it

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def plusOne(self, digits: List[int]) -> List[int]:
    digits = digits[::-1]
    one, i = 1, 0

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(1)
            one = 0
        i += 1

    return digits[::-1]
```