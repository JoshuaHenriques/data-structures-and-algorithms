# 46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

*Example 1:*

```
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
```

*Example 2:*

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

*Example 3:*

```
Input: nums = [1]
Output: [[1]]
```

*Constraints:*

```
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
```

## Solution

### Approach
We want to break up our input array by poping an element and recursively call the function to get the permutations of that smaller array. The base case is when we reach a single element in the array and we return it back up as an array of an array. We append back the element to that array and then we pop again to find the permutations on the other element. When we get back up to the initial recursively call we add back the element we popped off to each of the results that came back up. We repeat this process for every element in the array.

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def permute(self, nums: List[int]) -> List[List[int]]:
    result = []


    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    
    return result
```