# 735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

*Example 1:*

```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

*Example 2:*

```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

*Example 3:*

```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

*Constraints:*

* 2 <= asteroids.length <= 104
* -1000 <= asteroids[i] <= 1000
* asteroids[i] != 0

## Solution

### Approach
For each asteroid we check if the stack isn't empty, the current asteroid is moving left and the top of the stack is moving right. If true then we know there is a collision, if the current asteroid plus the top of the stack is less than 0 then we know the asteroid was bigger and we can pop from the stack. If the difference is greater than zero then we know the asteroid was smaller and we destroy it by setting it to 0. If they are the same size we assign it to 0 and pop from the stack. Otherwise if the asteroid wasn't already destroyed we push it to the stack.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                a = 0
                stack.pop()

        if a:
            stack.append(a)

    return stack
```
