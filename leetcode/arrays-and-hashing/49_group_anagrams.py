def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)

    return hashmap.values()

def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        # lists can't be keys
        hashmap[tuple(count)].append(word)

    return hashmap.values()