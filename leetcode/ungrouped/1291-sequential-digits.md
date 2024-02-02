# 1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

*Example 1:*

```
Input: low = 100, high = 300
Output: [123,234]
```

*Example 2:*

```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

*Constraints:*

* 10 <= low <= high <= 10^9

## Naive Solution (TLE)

### Approach
Iterate through the range from low to high and convert each number into a string and iterate through that number to check if it has sequential digits.

### Complexity
$$Time: O(n*len(str(high)))$$

$$Space: O(n)$$

### Code
```py
def sequentialDigits(self, low: int, high: int) -> List[int]:
    res = []

    for i in range(low, high + 1):
        num = [int(c) for c in str(i)]
        
        flag = True
        for j in range(len(num) - 1):
            if num[j] + 1 != num[j + 1]:
                flag = False 

        if flag:
            res.append(int(''.join(map(str, num))))

    return res
```

## Solution 1

### Approach
Generate all sequential digits within the low-high range by digit lengths. Iterate through the number of digits between low and high and at each iteration we start building all sequential digits from 1-9. If that start digit plus the total number of digits we're at is over 10 we can skip it. (6789 works but 789[10] doesn't work) We build the number by looping through the remaining digits in the current number we're building and multiply by 10 to shift the number and add prev by 1 and add it to the current number. (6 * 10 + (6 + 1) -> 67 -> 678 -> 6789) After that we append to the result array if it's within the low and high bounds.

### Complexity
$$Time: O(1)$$

$$Space: O(n)$$

### Code
```py
def sequentialDigits(self, low: int, high: int) -> List[int]:
    res = []
    lowDigit, highDigit = len(str(low)), len(str(high))

    for digits in range(lowDigit, highDigit + 1):
        for start in range(1, 9):
            if start + digits > 10:
                break
            
            num = start
            prev = start
            print(start)
            for i in range(digits - 1):
                print(num, prev)
                num = num * 10
                prev += 1
                num += prev
                print(num, prev)

            if low <= num <= high:
                res.append(num)

    return res
```

## Solution 2

### Approach
Clever trick is to use a queue data structure to help maintain a sorted result. Refer to Neetcode video

### Complexity
$$Time: O(1)$$

$$Space: O(n)$$

### Code
```py
def sequentialDigits(self, low: int, high: int) -> List[int]:
    res = []
    queue = deque(range(1, 10))

    while queue:
        n = queue.popleft()

        if n > high:
            continue
        if low <= n <= high:
            res.append(n)
        
        ones = n % 10
        if ones < 9:
            queue.append(n * 10 + (ones + 1))

    return res
```