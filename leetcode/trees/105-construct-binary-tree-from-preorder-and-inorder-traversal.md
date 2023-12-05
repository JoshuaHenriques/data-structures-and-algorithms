# 105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

*Example 1:*

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

*Example 2:*

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

*Constraints:*

```
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
```

## Solution

### Approach (rewatch video)
A preorder array's first element will always be the root node of the tree and the second element will always be the root of the left child node. In an inorder array, the elements that come before the root node's value is in the left subtree and the elements that are after it is in the right subtree. We can call the index of the root node in the inorder array the mid way point between the left subtree elements and right subtree elements. We use recursion to generate root.left using the preorder subarray starting from index one to skip the "root" value up until the "mid + 1" (python slicing is noninclusive) and the inorder subarray starting from the start of the array up until the "mid + 1". To generate the root.right it uses the preorder and inorder subarray starting from "mid + 1" until the end of the array.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root
```