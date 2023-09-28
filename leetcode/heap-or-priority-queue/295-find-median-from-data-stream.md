# 295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

*Example 1:*

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

*Constraints:*

```
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
```

## Solution

### Approach
Naive approach would be to use one array and when we insert an element we do it in order which is O(n). A more efficent way is to two heaps to split the large numbers from the smalls numbers. The large heap will be our minheap and the small heap will be our max heap. This helps us keep our add number function at O(logn) instead of O(n). While we're inserting numbers theres a few cases we have to worry about: Both heaps should be approximately equal (keeping a 1 element different) if not we choose the heap with more elements and get the minimum value (if its the large heap) or the maximum value (if its the small heap), remove it, and insert it into the other heap. All elements in the small heap (maxheap) should be less than the minimum value in the large heap (minheap), if not we take the min/max value, remove it, and insert it into the other heap.

### Complexity
$$Time: O(logn)$$

$$Space: O()$$

### Code
```
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # multiple by -1 to make a maxheap since python doesn't support it
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # uneven size, difference is greater than 1
        if len(self.small) > len(self.large) + 1:
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1: 
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * value)
            
    def findMedian(self) -> float:
        # is odd number of total elements and the small heap has more
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        # is odd number of total elements and the large heap has more
        if len(self.large) > len(self.small):
            return self.large[0]

        # is even number of total elements so we take the min and max value and divide by 2
        return (-1 * self.small[0] + self.large[0]) / 2
```