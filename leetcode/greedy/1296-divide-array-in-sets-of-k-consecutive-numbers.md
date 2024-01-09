# 1296. Divide Array in Sets of K Consecutive Numbers
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

*Example 1:*

```
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
```

*Example 2:*

```
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
```

*Example 3:*

```
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
```

*Constraints:*

```
1 <= k <= nums.length <= 105
1 <= nums[i] <= 109
```

## Optimized Solution

### Approach
Group frequency of values in a hashmap and have a minHeap of all the distinct values. We need to know the minimum value since we will always need one at the start of a group. When creating our groups if a consecutive number doesn't exist or if our count for that number is at 0 we can return False. Each time we group numbers we adjust the count in the hashmap or pop it from the hashmap but if the number we're popping is not the minimum number then we can return False since the next group will be missing a number.

### Complexity
$$Time: O(lognn)$$

$$Space: O(n)$$

### Code
```py
def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    if len(nums) % k != 0:
        return False

    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1

    minH = list(freq.keys())
    heapq.heapify(minH) 
    while minH:
        first = minH[0]

        for i in range(first, first + k):
            if i not in freq:
                return False
            freq[i] -= 1
            if freq[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)

    return True
```
