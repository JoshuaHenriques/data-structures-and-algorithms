# 1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

*Example 1:*

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

*Example 2:*

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

*Example 3:*

```
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```

*Constraints:*

```
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
```

## Naive Solution

### Approach
Using dfs helper function with the parameter curr which is an array of the past values in the path. Each recursive call we check if the root value is greater or equal to the values before it by looping through the current path array. Using preorder traversal we check if the root node is "good" then we recursively call dfs on the left and right subtree with a copy of the current path that has that root.value appended to it.

### Complexity
$$Time: O(n*h)$$

$$Space: O(n)$$

### Code
```
def goodNodes(self, root: TreeNode) -> int:
    good = 1

    def dfs(root, curr):
        nonlocal good
        if not root:
            return
        
        goodBool = True
        for n in curr:
            if root.val < n:
                goodBool = False
        good += 1 if goodBool else 0

        curr.append(root.val)
        dfs(root.left, curr.copy())
        dfs(root.right, curr.copy())

    dfs(root.left, [root.val])
    dfs(root.right, [root.val])
    return good
```

## Optimized Solution

### Approach
Same approach as above but instead of keeping track of a current array that holds the node values and looping through it each time we keep track of the maximum value on the current path and just check the root value against that one value which is a constant operation.

### Complexity
$$Time: O(h)$$

$$Space: O(n)$$

### Code
```
def goodNodes(self, root: TreeNode) -> int:
    good = 1

    def dfs(root, maxVal):
        nonlocal good
        if not root:
            return

        if root.val >= maxVal:
            good += 1
        
        dfs(root.left, max(root.val, maxVal))
        dfs(root.right, max(root.val, maxVal))

    dfs(root.left, root.val)
    dfs(root.right, root.val)
    return good
```