# 179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

*Example 1:*

```txt
Input: nums = [10,2]
Output: "210"
```

*Example 2:*

```txt
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

*Constraints:*

```txt
1 <= nums.length <= 100
0 <= nums[i] <= 109

```

## Solution

### Approach

A clever way to check for the largest number is to sort the array by comparing the two ways to concat the interger strings to form the next number. For example: 9534330 -> 9534___ -> "3" + "30" vs "30" + "3". Create a custom compare function that checks and compares both ways to form the next numbers forming the largest number.

### Complexity

$$Time: O(nlogn)$$

$$Space: O(1)$$

### Code

```py
def largestNumber(self, nums: List[int]) -> str:
    for i, n in enumerate(nums):
        nums[i] = str(nums[i])

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key=cmp_to_key(compare))

    return str(int("".join(nums))) 
```

