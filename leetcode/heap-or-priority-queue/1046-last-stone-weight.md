# 1046. Last Stone Weight
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

*Example 1:*

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

*Example 2:*

```
Input: stones = [1]
Output: 1
```

*Constraints:*

```
1 <= stones.length <= 30
1 <= stones[i] <= 1000
```

## Naive Solution

### Approach
Straight forward naive approach.

### Complexity
$$Time: O(n*nlogn)$$

$$Space: O(1)$$

### Code
```
def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort()

    if len(stones) == 2:
        if stones[0] == stones[1]:
            stones.pop()
            stones.pop()
        else:
            stones[0] = stones[1] - stones[0]
            stones.pop()

    if len(stones) == 2:
        return stones[0]

    i = len(stones) - 1
    while i > 0:
        if i - 1 >= 0:
            print(i)
            if stones[i] == stones[i-1]:
                stones.pop()
                stones.pop()
                i -= 2
            else:
                stones[i-1] = stones[i] - stones[i-1]
                stones.pop()
                i -= 1
        
        stones.sort()
    
    return stones[0] if len(stones) > 0 else 0
```

## Optimized Solution

### Approach
Since we need to get maximums of the array it would be more efficent to use a heap data structure to solve this problem. Converting the array to a heap is O(n). Note that there is no native maxheaps in python so we have to convert the values to negatives to simulate it. The algorithm is straight forward, we just make sure to get the absolute values when poping elements and multiplying by negative when pushing elements. Poping and pushing is done in O(logn). We append 0 into the heap just incase the heap is empty before returning

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```
def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones) # O(n)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones)) # O(nlogn)
        second = abs(heapq.heappop(stones))

        if second < first:
            heapq.heappush(stones, -1 * (first - second))

    stones.append(0)
    return abs(stones[0])
```