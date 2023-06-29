def longestConsecutive(self, nums: List[int]) -> int:
    # has to be a set for O(1) loop up time vs O(n) loopup time for lists
    nums_set = set(nums)

    if len(nums) == 0:
        return 0
    max_count = 1
    for n in nums:
        count = 0
        if n-1 in nums_set:
            continue
        elif n-1 not in nums_set:
            count += 1
            next_num = n+1
            if next_num not in nums_set:
                continue
            while (next_num in nums_set):
                count += 1
                next_num += 1

        if count > max_count:
            max_count = count
        
        count = 0

    return max_count

def longestConsecutive2(self, nums: List[int]) -> int:
    # has to be a set for O(1) loop up time vs O(n) loopup time for lists
    num_set = set(nums)
    max_seq = 0

    for n in nums:
        # check if start of sequence
        if n-1 not in num_set:
            count = 1
            while n+count in num_set:
                count += 1
            max_seq = max(count, max_seq)
    
    return max_seq