# 114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

* The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
* The "linked list" should be in the same order as a pre-order traversal of the binary tree.


*Example 1:*

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

*Example 2:*

```
Input: root = []
Output: []
```

*Example 3:*

```
Input: root = [0]
Output: [0]
```

*Constraints:*

* The number of nodes in the tree is in the range [0, 2000].
* -100 <= Node.val <= 100


## Naive Solution

### Approach

Create array of nodes using a preorder traversal helper function. Iterate through array of nodes, set each left child to null and assign the next node always to the right child.

### Complexity

$$Time: O(n)$$

$$Space: O(n)$$

### Code

```py
def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    preOrderArr = []

    def preOrderTraversal(root):
        if not root:
            return

        preOrderArr.append(root)

        if root.left:
            preOrderTraversal(root.left)

        if root.right:
            preOrderTraversal(root.right)

    preOrderTraversal(root)

    for node in preOrderArr:
        if root == node:
            continue
        
        root.left = None
        root.right = node
        root = root.right
```

## Optimized Solution

### Approach

The helper function flattens the root tree and returns the lists tail. We recursively call this function on the left and right subtree in order to get the tail of both. To connect them to the root we only care about the edge involving the left subtree not being null because if the right subtree is null we still have to move the left subtree and if the left subtree is null we don't have to do anything. To insert the left subtree to the right we first take the right tree and append it to the tail.right of the flatten left subtree then the root.right will be the head of the left subtree and then we set the root.left to None. When we return the tail node its in the order of the rightTail if its not null but if it is then it'll be the left tail and if both are null it will be the root

### Complexity

$$Time: O(n)$$

$$Space: O(h)$$

### Code

```py
def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    def dfs(root):
        if not root:
            return None

        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        # rightTail would be the linkedlist but if null then the leftTail would be it and if not that it would be just the root
        last = rightTail or leftTail or root
        return last

    dfs(root)
```
