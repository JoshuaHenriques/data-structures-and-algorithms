from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashmap to keep a counter on the nums in the array
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        
        return False