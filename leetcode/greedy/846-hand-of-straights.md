# 846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

*Example 1:*

```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
```

*Example 2:*

```
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
```

*Constraints:*

```
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
```

## Greedy Solution

### Approach
Group frequency of values in a hashmap and have a minHeap of all the distinct values. We need to know the minimum value since we will always need one at the start of a group. When creating our groups if a consecutive number doesn't exist or if our count for that number is at 0 we can return False. Each time we group numbers we adjust the count in the hashmap or pop it from the hashmap but if the number we're popping is not the minimum number then we can return False since the next group will be missing a number.

### Complexity
$$Time: O(lognn)$$

$$Space: O(n)$$

### Code
```py
def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    freq = defaultdict(int)

    for num in hand:
        freq[num] += 1

    minH = list(freq.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]

        for i in range(first, first + groupSize):
            if i not in freq:
                return False
            freq[i] -= 1
            if freq[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)

    return True
```
