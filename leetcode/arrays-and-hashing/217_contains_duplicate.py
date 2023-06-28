def containsDuplicate(nums: List[int]) -> bool:
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    
    return False

def containsDuplicate2(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)

    return False

def containsDuplicate3(nums: List[int]) -> bool:
    nums.sort()
    j = 1
    for i in range(len(nums)):
        if j == len(nums):
            return False
        elif nums[i] == nums[j]:
            return True
        j += 1

print(containsDuplicate(nums))