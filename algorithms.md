# Algorithms/Patterns

## Two Pointers
* This technique is commonly applied on sorted arrays or linked lists to find pairs or reverse elements. It is an ideal strategy when managing elements with pair relationships.
* Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition.Two Pointers is often useful when searching pairs in a sorted array or linked list; for example, when you have to compare each element of an array to its other elements.

#### Identifying Pattern 
* It will feature problems where you deal with sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints
* The set of elements in the array is a pair, a triplet, or even a subarray

## Sliding Window
* This pattern is used to track a subset of data within a larger dataset. It's particularly useful in array or string problems when you need to maintain a 'window' of elements satisfying a certain condition.
* Used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.

#### Identifying Pattern 
* The problem input is a linear data structure such as a linked list, array, or string
* You’re asked to find the longest/shortest substring, subarray, or a desired value

## Binary Search
* Can be used on Trees and Arrays
* Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, the best algorithm you can use is the Binary Search.

* The patterns looks like this for an ascending order set:
    1. First, find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: middle = start + (end — start) / 2
    2. If the key is equal to the number at index middle then return middle
    3. If ‘key’ isn’t equal to the index middle:
    4. Check if key < arr[middle]. If it is reduce your search to end = middle — 1
    5. Check if key > arr[middle]. If it is reduce your search to end = middle + 1

## Fast & Slow Pointer (Floyd's Tortoise and Hare Algorithm)
* A pointer algorithm that uses only two pointers, which move through the sequence at different speeds.
* Used in linked list or array problems, this pattern is ideal for detecting cycles or finding a midpoint.
* By moving at different speeds (say, in a cyclic linked list), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

#### Identifying Pattern
* The problem will deal with a loop in a linked list or array
* When you need to know the position of a certain element or the overall length of the linked list.

## Tree Traversal

### Pre-Order Traversal
* RRL Root -> Right -> Left

### Post-Order Traversal
* RLR Right -> Left -> Root

### In-Order Traversal
* RRL Right -> Root -> Left

## Breadth First Search
* Can be used on Trees and Graphs
* For traversing a tree level-by-level or a graph, providing a comprehensive overview of all nodes or cells.

### Tree BFS
* Traverse a tree and uses a queue to keep track of all the nodes of a level before jumping onto the next level
* The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.

### Graph BFS
* Multiple/simultaneous bfs
    * 994 Rotting Oranges
    * 286 Walls and Gates

#### Identifying Pattern
* If you’re asked to traverse a tree in a level-by-level fashion (or level order traversal)


## Depth First Search
* Can be used on Trees and Graphs
* This pattern allows you to traverse a tree or graph using depth as the main factor.

### Tree DFS
* You can use recursion (or a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.
* The Tree DFS pattern works by starting at the root of the tree, if the node is not a leaf you need to do three things:
    * Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order).
    * Make two recursive calls for both the children of the current node to process them.

#### Identifying Pattern
* If you’re asked to traverse a tree with in-order, preorder, or postorder DFS
* If the problem requires searching for something where the node is closer to a leaf

## Tries
* Ideal for efficient retrieval of keys in a dataset of strings. It's commonly used for features like autocomplete or spell check.


## Heap / Priority Queue
* Ideal when dealing with situations that require access to both the smallest and largest elements simultaneously. 
* In many problems, we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part.
* This pattern uses two heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element. The pattern works by storing the first half of numbers in a Max Heap, this is because you want to find the largest number in the first half. You then store the second half of numbers in a Min Heap, as you want to find the smallest number in the second half. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

### Identifying Pattern
* Useful in situations like Priority Queue, Scheduling
* If the problem states that you need to find the smallest/largest/median elements of a set
* The best data structure to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements.
* Whenever you’re given ‘K’ sorted arrays, you can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays.

## Backtracking
* Recursion 
* Decision Trees
* permutations and combinations

### Subsets
* Involve dealing with Permutations and Combinations of a given set of elements.

### 0/1 Knapsack
* Useful in solving problems related to permutations and combinations.

## Topological Sort
* Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, vertex u comes before v in the ordering.
* A course has 3 possible states:
    * visited -> crs has been added to the output
    * visiting -> crs not added to output, but added to cycle
    * unvisited -> crs not added to output or cycle
* A valid topological ordering can be computed by reversing the DFS postorder traversal starting from a vertex with no incoming edges. In case not every vertex is reachable from the starting vertex, it's necessary to “restart” the reverse DFS postorder traversal from another vertex with no incoming edges.

## Union Find
* An algorithm that implements find and union operations on a disjoint set data structure. It finds the root parent of an element and determines whether if two elements are in the same set or not. If two elements are at different sets, merge the smaller set to the larger set.
* Two sets are called disjoint sets if they don’t have any element in common, the intersection of sets is a null set.

## Dijkstra's Algorithm
* Finds the shortest path between a given node (which is called the "source node") and all other nodes in a graph. This algorithm uses the weights of the edges to find the path that minimizes the total distance (weight) between the source node and all other nodes.
* BFS but with a min heap

### Path Compression
* There are several algorithms for Find that achieve the asymptotically optimal time complexity. One family of algorithms, known as path compression, makes every node between the query node and the root point to the root.

## 1-D Dynamic Programming


## 2-D Dynamic Programming


## Greedy


## Quick Select


## Intervals
* Use this pattern to deal with overlapping intervals, helping to create a more organized and efficient structure.
* In a lot of problems involving intervals, you either need to find overlapping intervals or merge intervals if they overlap.

#### Interval Relations
* 'a' and 'b' do not overlap
* 'a' and 'b' overlap, 'b' ends after 'a'
* 'a' completely overlaps 'b'
* 'a' and 'b' overlap, 'a' ends after 'b'
* 'b' completely overlaps 'a'
* 'a' and 'b' do not overlap

#### Identifying Pattern
* If you’re asked to produce a list with only mutually exclusive intervals
* If you hear the term “overlapping intervals”

## Math & Geometry


## Bit Manipulation