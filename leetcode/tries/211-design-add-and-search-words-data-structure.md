# 211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
* WordDictionary() Initializes the object.
* void addWord(word) Adds word to the data structure, it can be matched later.
* bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

*Example 1:*

```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

*Constraints:*

```
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
```

## Solution

### Approach
Everything else is similar to a regular implementation of a Trie tree except the search funciton. Using a dfs helper function, we loop through the characters in the word starting from the index provided from the dfs helper function parameter and if that word is a regular character we check if its in curr.children and either update the curr pointer or return false. If the character is a "." we would go through every child in the curr's children's (their values, so their nodes) and recursively call dfs on it. Our dfs paramenters would need the remaining portion of the word we're trying to match so we pass in the index i from our for loop on the word plus one since we're going down a child (skipping the ".") and the other parameter would be the child node. If dfs returns true for any of the children then we can return true otherwise if it exhausted the child loop then we can return False. If we had a regular word then we would use the iterative portion of the dfs helper function and if the for loop is exhausted we would return the curr node isEndOfWord boolean.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isWord = True

    def search(self, word: str) -> bool:
        def helper(j, root):
            curr = root

            for i in range(j, len(word)):
                if word[i] == ".":
                    for node in curr.children.values():
                        if helper(i + 1, node):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            
            return curr.isWord
        return helper(0, self.root)
```