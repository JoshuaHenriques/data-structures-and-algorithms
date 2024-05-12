# 1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

*Example 1:*

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
```

*Example 2:*

```
Input: root = [2,1,3]
Output: [2,1,3]
```

*Constraints:*

* The number of nodes in the tree is in the range [1, 104].
* 1 <= Node.val <= 105


## Solution

### Approach

First get an array representation of the binary search tree by doing an in order traversal. Second we will recursivley build the tree with the parameters of two points. Each step we'll calculate the mid element in the array and use that as the root node then the elements to the left of that element will be on in the left subtree and the right elements will be in the right subtree. 

### Complexity

$$Time: O(n)$$

$$Space: O(n)$$

### Code

```py
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inOrderArr = []
        self.inOrderTraversal(root, inOrderArr)
        return self.createBST(0, len(inOrderArr) - 1, inOrderArr)
        
    def inOrderTraversal(self, root, arr):
        if not root:
            return None

        self.inOrderTraversal(root.left, arr)
        arr.append(root.val)
        self.inOrderTraversal(root.right, arr)

    def createBST(self, left, right, arr):
        if left > right:
            return None

        mid = (left + right) // 2

        head = TreeNode(arr[mid])
        head.left = self.createBST(left, mid - 1, arr)
        head.right = self.createBST(mid + 1, right, arr)

        return head
```
