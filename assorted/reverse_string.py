from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Two pointer question
        # s.reverse()
        # s[:] = s[::-1]
        # s[::] = s[::-1]
        # print(s[-4])
        for i in range(len(s)//2): 
            # s[i], s[-i-1] = s[-i-1], s[i]
            s[i]. s[~i] = s[~i], s[i]
            print(f'-i-1: {-i-1}')