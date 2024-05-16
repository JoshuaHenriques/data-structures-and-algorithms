# 450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.


*Example 1:*

```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

*Example 2:*

```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

*Example 3:*

```
Input: root = [], key = 0
Output: []
```

*Constraints:*

* The number of nodes in the tree is in the range [0, 104].
* -105 <= Node.val <= 105
* Each node has a unique value.
* root is a valid binary search tree.
* -105 <= key <= 105


## Solution

### Approach

First search for the key by moving to the left or right substree depending if the key is greater than the root or not. Once we find the node with the key we can do one of three things: if there is no left subtree return the right subtree, vice versa, and if there is a left and right subtree we swap the current nodes value with the minimum value node in the right subtree then delete it by recursively calling the delete node function. Doing this deletes the initial key in the tree while satisfying the BST rules/properties.

### Complexity

$$Time: O(h)$$

$$Space: O(h)$$

### Code

```py
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None

    if key > root.val:
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # find min in right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

    return root 
```