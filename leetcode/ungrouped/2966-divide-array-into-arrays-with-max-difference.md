# 2966. Divide Array Into Arrays With Max Difference
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

* Each element of nums should be in exactly one array.
* The difference between any two elements in one array is less than or equal to k.

Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

*Example 1:*

```
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
```

*Example 2:*

```
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
```

*Constraints:*

* n == nums.length
* 1 <= n <= 105
* n is a multiple of 3.
* 1 <= nums[i] <= 105
* 1 <= k <= 105


## Solution

### Approach
Sort the input array. If the size of the array is not divisible by 3 then return an empty array. Iterate through the array and append the subarray's of size 3 into the result array. Iterate through the result to check if each element has at most difference of size k.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    if len(nums) % 3 != 0:
        return []
    
    res = []

    nums.sort()
    i, j = 0, 2
    while j < len(nums):
        res.append(nums[i:j + 1])
        i = j + 1
        j += 3

    for x in range(len(res)):
        if res[x][2] - res[x][1] > k or res[x][2] - res[x][0] > k or res[x][1] - res[x][0] > k:
            return []

    return res 
```

## Solution 2

### Approach
Same as above but written differently.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(0, len(nums), 3):
        if nums[i + 2] - nums[i] > k:
            return []
        res.append(nums[i:i + 3])

    return res
```
