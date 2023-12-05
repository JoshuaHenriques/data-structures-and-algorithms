# 739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

*Example 1:*

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

*Example 2:*

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

*Example 3:*

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

*Constraints:*

```
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
```

## Naive Solution (Time Limit Exceeded)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^2)$$

$$Space: O(n)$$

### Code
```
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    break
            if len(result) != i+1:
                result.append(0)

        return result
```

## Optimized Solution

### Approach
Monotonic Decreasing Stack

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # hold temperature and index
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append([t, i])

        return result
```