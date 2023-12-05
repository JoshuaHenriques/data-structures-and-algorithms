# 102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

*Example 1:*

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

*Example 2:*

```
Input: root = [1]
Output: [[1]]
```

*Example 3:*

```


Input: root = []
Output: []

```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
```

## Iterative BFS Solution

### Approach
To do this problem iteratively we can use a queue to store the nodes at each level. We can loop through the queue while the queue isn't empty and append the nodes on that level to a resulting array 

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return root

    queue = deque([root ])
    res = []

    while queue:
        arr = []
        for i in range(len(queue)):
            node = queue.popleft()
            arr.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(arr)
    
    return res
```