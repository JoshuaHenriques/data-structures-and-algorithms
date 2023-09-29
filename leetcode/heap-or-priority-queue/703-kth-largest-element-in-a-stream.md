# Question Name
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
* KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
* int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

*Example 1:*

```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

*Constraints:*

```
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
```

## Naive Solution

### Approach
Straight forward

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[-self.k]
```

## Optimized Solution

### Approach
The efficient way of solving this problem is using a heap data structure. The heap will be of size k because the question only wants the kth largest element so storing elements that is less than the kth largest element wouldn't ever be the kth largest (especially since in this problem we only add elements). Using a minheap lets us efficently pop the smallest element on the top whenever we add an element to the heap so we can keep it at size k. So to get the kth largest element we know it'll always be the minimum of the elements in the minheap so at the top of it.

### Complexity
$$Time: O(logn)$$

$$Space: O(n-k)$$

### Code
```
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
```