# 124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

*Example 1:*

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

*Example 2:*

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

*Constraints:*

```
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
```

## Solution

### Approach
Using recursion we can do a postorder traversal to compute the max path sum with a split and without a split. A split would be where we get the summation of the root node value with the left and right child values and without a split is the summation of the root node value and the max between the left subtrees max summation and the right subtrees max summation. Note that values can be negative so after we get the max of the right and left we reassign those with the max between itself and 0. We use a helper function to help with the state of the maxSum.

### Complexity
$$Time: O(n)$$

$$Space: O(h)$$

### Code
```
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    maxSum = [root.val]
    
    # return max path sum without split
    def helper(root):
        if not root:
            return 0

        leftMax = helper(root.left)
        leftMax = max(leftMax, 0)
        
        rightMax = helper(root.right)
        rightMax = max(rightMax, 0)

        # compute max path sum with split
        maxSum[0] = max(maxSum[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)

    helper(root)
    return maxSum[0]
```