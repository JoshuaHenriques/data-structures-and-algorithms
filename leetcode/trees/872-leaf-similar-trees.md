# Question Name
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

*Example 1:*

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

*Example 2:*

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

*Constraints:*

* The number of nodes in each tree will be in the range [1, 200].
* Both of the given trees will have values in the range [0, 200].

## Solution

### Approach
Using a helper function with root and the result array as parameters, we check the base case if root is null and then if both the left and right nodes are null. If so we know the current root node is a leaf and we can append it to our result array. Return the comparison of both arrays for the answer.

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # inorder traversal
    res1, res2 = [], []

    def helper(root, res):
        if not root:
            return

        if not root.left and not root.right:
            res.append(root.val)

        helper(root.left, res)
        helper(root.right, res)

    helper(root1, res1)
    helper(root2, res2)

    return res1 == res2
```