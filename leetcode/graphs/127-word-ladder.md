# 127. Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

*Example 1:*

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
```

*Example 2:*

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

*Constraints:*

```
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
```

## Naive Solution

### Approach
Double for loop to create the adjMap. Go through each word and compare it to each word to find words that differ by only one character.

## Optimized Solution

### Approach
To create the adjMap we go through each word and since each word shares the same length we loop through each character and swap it with a '\*' and use that pattern as the key in the adjMap and append words that fit that pattern into it. "hit" -> "h*t" and "hot" -> "h*t" would be grouped like: { "h*t": [hot, hit] } in the adjMap. Using bfs to traverse the graph if we end up on a node that is the endWord we can return the result. For the word/node that we're processing we get the patterns for that using the same method as before to get the adjacent words/nodes from the adjMap and add it to the visited set and queue then after that whole iteration of queue we increment the result.

### Complexity
$$Time: O(n^2*m)$$

$$Space: O()$$

### Code
```
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # words (nodes) are connected with the words in the word list that have a single character difference
    # build an adjMap to show the connections
    # naive solution, double for loop to create the adjMap O(n^2*m)
    if endWord not in wordList:
        return 0

    neighbours = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            neighbours[pattern].append(word)

    visited = set([beginWord])
    queue = deque([beginWord])
    result = 1

    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return result

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neigh in neighbours[pattern]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

        result += 1

    return 0
```