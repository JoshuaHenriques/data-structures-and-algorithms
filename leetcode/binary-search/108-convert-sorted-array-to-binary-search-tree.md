# 108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

*Example 1:*

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

*Example 2:*

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

*Constraints:*

* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums is sorted in a strictly increasing order.

## Solution

### Approach
Using a helper function to do this recursively, first check out base case if our left pointer is greater than our right pointer. Then we get our mid point and initialize it as our current root node, recursively call the helper function with the updated pointers for the left and right subtrees

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def helper(l, r):
        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = helper(l, mid - 1)
        root.right = helper(mid + 1, r)

        return root

    return helper(0, len(nums) - 1)
```