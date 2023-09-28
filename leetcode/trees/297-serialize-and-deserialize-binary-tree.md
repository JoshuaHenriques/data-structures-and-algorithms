# 297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

*Example 1:*

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

*Example 2:*

```
Input: root = []
Output: []
```

*Constraints:*

```
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000\
```

## DFS Solution

### Approach
We can use a preorder traversal array to help us deserialize and serialize a binary tree. To serialize we do a preorder traversal using a dfs helper function to create the result array by appending the root casted as a string. If we come across a null node we will add "N" in the array and for the rest we. We then return an array as a string. When we deserialize it we cast it back to an array and we initialize an index variable. In the dfs helper function we first check if the element we're at is null, if so, we increment the pointer and return null. If not, we create the node with the element, increment the pointer and recursively call dfs on the left and right node. Note that putting the character "N" in the array helps us know that we are at a leaf.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def serialize(self, root):
    res = []

    def dfs(node):
        if not node:
            res.append("N")
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(res)

def deserialize(self, data):
    values = data.split(",")
    self.i = 0

    def dfs():
        if values[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(values[self.i]))
        self.i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    
    return dfs()
```

## BFS Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```