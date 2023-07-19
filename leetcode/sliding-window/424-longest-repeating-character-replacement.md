# 424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

*Example 1:*

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

*Example 2:*

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
```

*Constraints:*

```
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
```

## Solution

### Approach
Create two pointer, i and j, that both start at index 0. Create a hashmap to store character frequency, a flag, and the current and max counter variables. Pass through the string and check if the flag is true so we can add the character to the hashmap and increase its frequency. To know the window of characters we're looking at is valid is when the window size minus the highest freq character is less than or equal to the input K. So if the window is valid then we can add to our counters and increase the window size (increment j). If the window we're on isn't valid then we decrement our counter, decrement the char at index i's freq from the hashmap, increment the i pointer to slide the window and change the flag to false we on our next iteration we don't readd the char at j's frequency

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def characterReplacement(self, s: str, k: int) -> int:
    i, j = 0, 0
    longest = 0
    max_longest = 0
    hashmap = defaultdict(int)
    flag = True

    while j < len(s):
        if flag:
            hashmap[s[j]] += 1
        flag = True
        highest_freq = hashmap[max(hashmap, key = hashmap.get)]
        if len(s[i:j+1]) - highest_freq <= k:
            longest += 1
            max_longest = max(max_longest, longest)
            j += 1
            continue
        else:
            longest -= 1
            hashmap[s[i]] -= 1
            i += 1
            flag = False
    
    return max_longest      
```

## Optimized Solution

### Approach
Same approach as above.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def characterReplacement(self, s: str, k: int) -> int:
    count = defaultdict(int)
    result = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] += 1

        while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
        
        result = max(result, r - l + 1)
    
    return result
```