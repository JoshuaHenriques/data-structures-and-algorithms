# Longest Consecutive Sequence

*Example 1:*

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

*Example 2:*

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

*Constraints:*

```
0 <= nums.length <= 105
-109 <= nums[i] <= 109
```

## Solution

### Approach
It's important to convert the array to a set for O(1) lookup. Iterate through the set, check if the element minus one is in the set. If so then we know that it's not the start of a sequence, if not then we know it's the start of a sequence. If we're at a start increment the counter and while the element plus one (or element plus the counter) is in the set we can go through the while loop again and increment the counter

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def longestConsecutive(self, nums: List[int]) -> int:
    # has to be a set for O(1) loop up time vs O(n) loopup time for lists
    num_set = set(nums)
    max_seq = 0

    for n in nums:
        # check if start of sequence
        if n-1 not in num_set:
            count = 1
            while n+count in num_set:
                count += 1
            max_seq = max(count, max_seq)
    
    return max_seq
```