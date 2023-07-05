def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hashmap = defaultdict(int)

    for i in nums:
        # or use hashmap.get(i, 0)
        hashmap[i] += 1

    values = list(hashmap.values())
    sorted_values = sorted(values)
    result = []

    for key in nums:
        if hashmap[key] in sorted_values[len(sorted_values)-k:] and key not in result:
            result.append(key)

    return result

def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
    hashmap = defaultdict(int)

    for i in nums:
        hashmap[i] += 1

    count = [[] for i in range(len(nums)+1)]
    for n, c in hashmap.items():
        count[c].append(n)
    
    result = []
    for i in range(len(count)-1, 0, -1):
        for j in range(len(count[i])):
            result.append(count[i][j])
            if len(result) == k:
                return result