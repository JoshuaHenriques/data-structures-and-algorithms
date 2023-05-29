from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()

        j = 1
        for i in range(len(nums)):
            if j == len(nums):
                return False
            elif nums[i] == nums[j]:
                return True
            j += 1