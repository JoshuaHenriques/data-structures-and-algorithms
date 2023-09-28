# 212. Word Search II
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

*Example 1:*

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

*Example 2:*

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

*Constraints:*

```
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
```

## Solution

### Approach
Similar to Word Search with a couple of differences. Since we're given a list of words, it's best to use a Trie to more efficently store and look up the words when needed. So first store all the words. Then we do a regular dfs approach with the current node and the current word (starting at ""). In the dfs helper function we check if row and col is out of bounds, if we've visited them before and if the character at that cell is a child of the current node we're on. If so add row and col to visited and update our curr pointer to that character, update the current word by adding the character to it then we can check if the new curr pointer is a word, if so add it to our results. Then we recursively call the dfs helper function on the adjacent cells

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWords(self, words: List[str]):
        for word in words:
            curr = self.trieRoot

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.addWords(words)

        ROWS = len(board)
        COLS = len(board[0])
        result, seen = set(), set()

        def dfs(row, col, curr, word):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return

            if (row, col) in seen:
                return

            if board[row][col] not in curr.children:
                return


            seen.add((row, col))

            curr = curr.children[board[row][col]]
            word += board[row][col]
            if curr.isWord:
                result.add(word)

            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in d:
                dfs(row + dr, col + dc, curr, word)

            seen.remove((row, col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, self.trieRoot, "")

        return result
```