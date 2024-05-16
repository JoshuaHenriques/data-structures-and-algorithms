# 1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

*Example 1:*

```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
```

*Example 2:*

```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

*Constraints:*

* The number of nodes in the tree is in the range [1, 104].
* -105 <= Node.val <= 105

## Solution

### Approach

Do a BFS traversal on the tree and at each layer we'll keep track of the level we're on and add to the current sum. After appending the next level to the queue we replace maximum sum and the result variable if current sum is greater.

### Complexity

$$Time: O(n)$$

$$Space: O(n)$$

### Code

```py
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    maxSum = 0
    res = 0
    queue = deque()

    if root:
        maxSum = root.val
        res = 1
        queue.append(root)

    cnt = 0
    while queue:
        cnt += 1
        currSum = 0
        for i in range(len(queue)):
            node = queue.popleft()
            currSum += node.val

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        if currSum > maxSum:
            res = cnt
            maxSum = currSum

    return res
```
