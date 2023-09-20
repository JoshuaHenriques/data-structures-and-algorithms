# 104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*Example 1:*

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

*Example 2:*

```
Input: root = [1,null,2]
Output: 2
```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
```

## DFS Solution

### Approach
Using depth first search we can keep adding the max between both recursive calls on the left and right child to get the total depth

### Complexity
$$Time: O(n)$$

$$Space: O(h)$$

### Code
```
def maxDepth(self, root: Optional[TreeNode]) -> int:
    depth = 1

    if not root:
        return 0

    depth += max(self.maxDepth(root.left), self.maxDepth(root.right))

    return depth
```

## Iterative DFS Solution

### Approach (Preorder)
Using a preorder iterative dfs approach we need a stack and each stack will hold the node and the current depth its on. Put the ```[root, 1]``` on the stack first and while stack isn't null we want to pop both the node and depth and first get the max between the popped depth and the current max depth. Check if the left and right child exist and add then to the stack with the popped depth + 1.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    mDepth = 1

    stack = [[root, 1]]
    while stack:
        node, depth = stack.pop()
        
        mDepth = max(mDepth, depth)
        
        if node.left:
            stack.append([node.left, depth + 1])

        if node.right:
            stack.append([node.right, depth + 1])
            
    return mDepth
```

## BFS Solution (Level order traversal)

### Approach
Using an iterative bfs approach we need a queue and each element will hold just a node. Starting with the root, if the queue isn't empty we increment the depth and run a for loop on the queue. In each loop iteration we'll pop the node off and add it's left and right children. As a note we wouldn't end up popping the children off the stack since the for loop len was before adding them

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    depth = 0
    queue = deque([root])
    while queue:
        depth += 1

        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    
    return depth
```