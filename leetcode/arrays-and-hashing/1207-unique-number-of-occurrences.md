# 1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

*Example 1:*

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

*Example 2:*

```
Input: arr = [1,2]
Output: false
```

*Example 3:*

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

*Constraints:*

* 1 <= arr.length <= 1000
* -1000 <= arr[i] <= 1000

## Solution

### Approach
Count the frequencies of each number. Convert those values into a set and if the set isn't the same length as the input array size then return True

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def uniqueOccurrences(self, arr: List[int]) -> bool:
    hashmap = defaultdict(int) 

    for num in arr:
        hashmap[num] += 1

    hashset = set(hashmap.values())
    
    return len(hashset) == len(hashmap)
```
