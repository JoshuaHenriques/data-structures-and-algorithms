def checkInclusion(self, s1: str, s2: str) -> bool:
    i, j = 0, len(s1) - 1
    # Use alphabet array for practice
    s1_hashmap = defaultdict(int)
    s2_hashmap = defaultdict(int)

    if len(s1) == 1 and s1 in s2:
        return True

    if len(s1) > len(s2):
        return False

    for char in s1:
        s1_hashmap[char] += 1

    for char in s2[i:j+1]:
        s2_hashmap[char] += 1

    while j < len(s2):
        if s1_hashmap == s2_hashmap:
            return True

        s2_hashmap[s2[i]] -= 1
        if s2_hashmap[s2[i]] == 0:
            s2_hashmap.pop(s2[i])
        i += 1
        j += 1

        if j < len(s2):
            s2_hashmap[s2[j]] += 1

    return False