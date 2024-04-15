# 1372. Longest ZigZag Path in a Binary Tree
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

*Example 1:*

```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
```

*Example 2:*

```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
```

*Example 3:*

```
Input: root = [1]
Output: 0
```

*Constraints:*

* The number of nodes in the tree is in the range [1, 5 * 104].
* 1 <= Node.val <= 100

## Solution

### Approach
With a helper function with the parameters: root, current direction, and current count. Set the total count the max between itself and the current count. If the current direction is right we recursively call the helper with the left node while incrementing the current count. We also call the helper function on the right node and reset the count. We do the opposite for the other direction. 

### Complexity
$$Time: O(n)$$

$$Space: O(logn)$$

### Code
```py
def longestZigZag(self, root: Optional[TreeNode]) -> int:
    self.total = 0
    
    def helper(root, currDir, currCnt):
        if not root:
            return

        self.total = max(self.total, currCnt)

        if currDir == "right":
            helper(root.left, "left", currCnt + 1)
            helper(root.right, "right", 1)
            return

        if currDir == "left":
            helper(root.right, "right", currCnt + 1)
            helper(root.left, "left", 1)
            return



    helper(root.left, "left", 1)
    helper(root.right, "right", 1)

    return self.total
```