def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_s, freq_t = {}, {}

    for i in range(len(s)):
        freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
        freq_t[t[i]] = 1 + freq_t.get(t[i], 0)

    for key in freq_s:
        if key not in freq_t:
            return False
        if freq_s[key] != freq_t[key]:
            return False
    
    return True

def isAnagram2(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    if s != t:
        return False

    return True