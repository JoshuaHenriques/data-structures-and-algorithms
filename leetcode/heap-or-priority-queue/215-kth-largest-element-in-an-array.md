# 215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

*Example 1:*

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

*Example 2:*

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

*Constraints:*

```
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
```

## Solution (Heapsort)

### Approach
Convert nums to a minheap and while the heap is greater than size k we can keep poping the top. Since this is a minheap we can simply pop off the top when the heap is size k to get the kth largest element

### Complexity
$$Time: O((n-k)logn)$$

$$Space: O(1)$$

### Code
```
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return heapq.heappop(nums)
```

## Solution (Quick Select)

### Approach
Quick select is similar to quick sort when it comes to finding a pivot point. k will be reassigned to what the index would be to get the kth element if the array was sorted. Define the quickselect helper function with the parameters being a left and right pointer that point to the partition of the array we're currently looking at. For the partition we assign pivot which will be the last element in the array and the p will be the left pointer. Iterate through the partition and if nums[i] is less than our nums[p] then we swap the elements and increment the p pointer. At the end of the loop swap the pivot element with the element at p. Now if k is less than p we recursively call the function of the left partition of p, k is greater we call it with the right partition of p, and if they're equal we have found the kth element

### Complexity
$$Time (Average): O(n)$$

$$Space: O(1)$$

### Code
```
def findKthLargest(self, nums: List[int], k: int) -> int:
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        nums[p], nums[r] = nums[r], nums[p]

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]

    return quickSelect(0, len(nums) - 1)
```