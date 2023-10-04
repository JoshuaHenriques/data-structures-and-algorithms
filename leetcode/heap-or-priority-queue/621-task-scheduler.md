# 621. Task Scheduler
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

*Example 1:*

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

*Example 2:*

```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

*Example 3:*

```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

*Constraints:*

```
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
```

## Optimized Solution

### Approach
Get the frequencies of characters and start processing the most frequent character. Using a maxheap we can keep track which character has the most left to be processed by the CPU. We start by popping from the maxheap, decrement that freq by one, add the idle time to the current time to figure out when that character is available again, and push those two values into a queue. We keep doing this until the current time matches the time available of the element in the top of the stack and then push it back into the maxheap. If the time available reach zero we don't need to add it into the queue. 

### Complexity
$$Time: O(len(tasks)*n)$$

$$Space: O(n)$$

### Code
```
def leastInterval(self, tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxheap = [-cnt for cnt in count.values()]

    heapq.heapify(maxheap)
    time = 0
    queue = deque() # pairs of [-cnt, idleTime/timeAvailable]

    while maxheap or queue:
        time += 1

        if maxheap:
            cnt = 1 + heapq.heappop(maxheap) # cnt is negative
            if cnt != 0:
                queue.append([cnt, time + n])

        if queue and queue[0][1] == time:
            heapq.heappush(maxheap, queue.popleft()[0])

    return time
```