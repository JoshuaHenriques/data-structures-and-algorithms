# 230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

*Example 1:*

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

*Example 2:*

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

*Constraints:*

```
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
```

## DFS Solution

### Approach
The question is asking to get the kth smallest element in the tree. So if were were to think of the tree as a sorted array we would get the k-1 indexed element. So we use the inorder traversal since that always comes out to a sorted array and we just return the sorted_arr[k-1] to get the answer.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    sorted_arr = []
    def helper(root):
        if root.left:
            helper(root.left)   

        sorted_arr.append(root.val)

        if root.right:
            helper(root.right)

    helper(root)
    return sorted_arr[k-1]
```

## Iterative DFS Solution

### Approach
Same as above but we use a stack to do this inorder (LRR) traversal iteratively. We use a while loop to keep going to the left child until null then we can process the node.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
            
        curr = curr.right
```