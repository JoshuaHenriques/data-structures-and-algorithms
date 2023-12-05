# 4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

*Example 1:*

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

*Example 2:*

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

*Constraints:*

```
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
```

## Naive Solution

### Approach
Simple merging. Answer technically wrong since done in O(n+m) time. 

### Complexity
$$Time: O(n+m)$$

$$Space: O(n+m)$$

### Code
```
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # O(m+n) solution
    p1 = 0
    p2 = 0
    merged = []
    
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            merged.append(nums1[p1])
            p1 += 1
        else:
            merged.append(nums2[p2])
            p2 += 1

    if p1 == len(nums1):
        merged = merged + nums2[p2:]
    elif p2 == len(nums2):
        merged = merged + nums1[p1:]

    if len(merged) % 2 == 1:
        return merged[(len(merged) - 1) // 2]
    else:
        return (merged[(len(merged) - 1) // 2] + merged[((len(merged) - 1) // 2) + 1]) / 2

    return res
```

## Optimized Solution

### Approach
We make sure that the A array is the smallest so we compare and reassign if we have to. We want our left partition is be close to half the total lengths of both arrays.

### Complexity
$$Time: O(log(n+m))$$

$$Space: O(1)$$

### Code
```
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
```