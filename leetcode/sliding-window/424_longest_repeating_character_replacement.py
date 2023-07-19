def characterReplacement(self, s: str, k: int) -> int:
    i, j = 0, 0
    longest = 0
    max_longest = 0
    hashmap = defaultdict(int)
    flag = True

    while j < len(s):
        if flag:
            hashmap[s[j]] += 1
        flag = True
        highest_freq = hashmap[max(hashmap, key = hashmap.get)]
        if len(s[i:j+1]) - highest_freq <= k:
            longest += 1
            max_longest = max(max_longest, longest)
            j += 1
            continue
        else:
            longest -= 1
            hashmap[s[i]] -= 1
            i += 1
            flag = False
    
    return max_longest      

def characterReplacement2(self, s: str, k: int) -> int:
    count = defaultdict(int)
    result = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] += 1

        while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
        
        result = max(result, r - l + 1)
    
    return result