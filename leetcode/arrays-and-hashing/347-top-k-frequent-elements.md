# 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

*Example 1:*

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

*Example 2:*

```
Input: nums = [1], k = 1
Output: [1]
```

*Constraints:*

```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
```

## Solution 1

### Approach
Use a hashmap to record the frequency of the numbers in the array. Sort the list of frequencies from the hashmap and get the last k elements from that array.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hashmap = defaultdict(int)

    for i in nums:
        # or use hashmap.get(i, 0)
        hashmap[i] += 1

    values = list(hashmap.values())
    sorted_values = sorted(values)
    result = []

    for key in nums:
        if hashmap[key] in sorted_values[len(sorted_values)-k:] and key not in result:
            result.append(key)

    return result
```

## Solution 2

### Approach
Using an array we're going to use the index to represent the count/freq of the number and for each element will be the list of the numbers that have that count/freq

### Complexity
$$Time: O(n)$$
$$Space: O(n)$$

### Code
```
def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
    hashmap = defaultdict(int)

    for i in nums:
        hashmap[i] += 1

    count = [[] for i in range(len(nums)+1)]
    for n, c in hashmap.items():
        count[c].append(n)
    
    result = []
    for i in range(len(count)-1, 0, -1):
        for j in range(len(count[i])):
            result.append(count[i][j])
            if len(result) == k:
                return result
```