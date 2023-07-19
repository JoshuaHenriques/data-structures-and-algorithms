def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        max_longest = 1
        longest = 1

        if len(s) == 0:
            return 0

        while j < len(s):
            if s[j] in s[i:j]:
                longest = 1
                i += 1
                j = i + 1
            else:
                longest += 1
                j += 1

            max_longest = max(max_longest, longest)
        return max_longest