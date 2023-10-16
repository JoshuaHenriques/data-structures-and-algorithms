# 146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

*Example 1:*

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

*Constraints:*

```

```

## Naive Solution (Time Limit Exceeded 20 / 22)

### Approach
Straight forward approach. Just keeping track of the timestamp of each node so we can replace it when needed. Something needs to be optimized to avoid time limit exceeded.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
class ListNode:

    def __init__(self, key = None, value = None, timestamp = None):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = ListNode()
        self.capacity = capacity
        self.timestamp = 1
        self.items = 0

    # def print_cache(self):
    #     curr = self.cache
    #     print("print method")
    #     print(f"self.timestamp: {self.timestamp}")            
    #     print(f"self.items: {self.items}")            
    #     while curr:
    #         print("---")
    #         print(f"curr.key: {curr.key}")
    #         print(f"curr.value: {curr.value}")
    #         print(f"curr.timestamp: {curr.timestamp}")
    #         print("---")
    #         curr = curr.next
        

    def get(self, key: int) -> int:
        # print(f"get key: {key}")
        curr = self.cache
        while curr:
            if curr.key == key:
                curr.timestamp = self.timestamp
                # self.print_cache()
                self.timestamp += 1
                return curr.value
            curr = curr.next
        # self.print_cache()
        self.timestamp += 1
        return -1

    def put(self, key: int, value: int) -> None:
        # print(f'PUT: key: {key}, value: {value}')
        # check if key in cache
        curr = self.cache
        while curr:
            if curr.key == key:
                curr.value = value
                curr.timestamp = self.timestamp
                # self.print_cache()
                self.timestamp += 1
                return
            curr = curr.next

        # over/under capacity
        if self.items == self.capacity:
            # LRU algo
            # print(f"LRU")
            minTime = (self.timestamp + 1, -1)
            curr = self.cache
            while curr:
                if curr.timestamp < minTime[0]:
                    minTime = (curr.timestamp, curr.key)
                curr = curr.next

            curr = self.cache
            while curr:
                if curr.key == minTime[1]:
                    curr.key = key
                    curr.value = value
                    curr.timestamp = self.timestamp
                    self.timestamp += 1
                    break
                curr = curr.next
            # self.print_cache()
            
        else:
            # find open spot
            # print("Add freely")            
            curr = self.cache
            prev = None
            for i in range(self.items):
                prev = curr
                curr = curr.next

            if not curr:
                curr = ListNode()

            if prev:
                prev.next = curr

            curr.key = key
            curr.value = value
            curr.timestamp = self.timestamp
               
            self.items += 1
            # self.print_cache()
            self.timestamp += 1
```

## Optimized Solution

### Approach
Using a doubly-linked list, hashmap to map the key to node memory addresses, two pointers left for least recently used (left most of list) and right for most recently used. When inserting we append to the right and update the pointers to do so. When removing we use the input nodes prev and next point to help with updating the pointers to remove that node. In the get function we first remove it from the linked list and insert it back so we know it's the most recently used node and then return the value. In the put function if the key already exists we remove it and create a new node with the same key but different value then add to the hashmap and and insert it back into the list. Once we hit the capacity we remove the least recent used node by removing the left most node and remove it from the hashmap 

### Complexity
$$Time: O(1)$$

$$Space: O(1)$$

### Code
```
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to nodes
        
        # left=LRU, right=MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right of list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
           self.remove(self.cache[key])
           self.insert(self.cache[key])
           return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the cache(hashmap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```