# 437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

*Example 1:*

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```

*Example 2:*

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```

*Constraints:*

* The number of nodes in the tree is in the range [0, 1000].
* -109 <= Node.val <= 109
* -1000 <= targetSum <= 1000


## Solution

### Approach
Refer to a video

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    self.total = 0
    self.lookup = defaultdict(int)
    self.lookup[targetSum] = 1

    def dfs(root, curr):
        if not root:
            return 

        curr += root.val
        self.total += self.lookup[curr]
        self.lookup[curr + targetSum] += 1

        dfs(root.left, curr)
        dfs(root.right, curr)

        self.lookup[curr + targetSum] -= 1

    dfs(root, 0)
    return self.total
```
