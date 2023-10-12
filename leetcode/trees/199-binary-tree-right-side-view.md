# 199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

*Example 1:*

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

*Example 2:*

```
Input: root = [1,null,3]
Output: [1,3]
```

*Example 3:*

```
Input: root = []
Output: []
```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## Solution

### Approach
Using BFS to traverse the tree in level order we are able to see what the right side view is for the tree. As your traversing the front of the queue will always have the right side view node at each iteration. So append that value to our result array. 

### Complexity
$$Time: O(h)$$

$$Space: O(n)$$

### Code
```
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    result =  []
    queue = deque()

    if root:
        queue.append(root)
        result.append(root.val)

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if not node:
                continue
            
            if node.right:
                queue.append(node.right)
            
            if node.left: 
                queue.append(node.left)
        
        if queue:
            result.append(queue[0].val)
        
    return result
```