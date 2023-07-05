# 49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

*Example 1:*

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

*Example 2:*

```
Input: strs = [""]
Output: [[""]]
```

*Example 3:*

```
Input: strs = ["a"]
Output: [["a"]]
```

*Constraints:*

```
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
```

## Naive Solution

### Approach
Iterate through the list, group the words using a hashmap using the sorted string as the key and the list of words that when sorted equal the key

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)

    return hashmap.values()
```

## Optimized Solution

### Approach
For each string in list count the characters and store the count in an a-z count array and use that as the key in a hashmap with a list of the words that have the same a-z count array

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        # lists can't be keys
        hashmap[tuple(count)].append(word)

    return hashmap.values()
```