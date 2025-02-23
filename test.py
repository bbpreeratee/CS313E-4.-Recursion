def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    mul5 = []
    i = 0
    nums = nums[start:]
    if len(nums) == 1 and target == 0:
        return True

    while i < len(nums):
        if nums[i] % 5 == 0:
            mul5.append(nums[i])
            if i+1 < len(nums) and nums[i+1] == 1: #ลองลบ
                nums.pop(i+1)
        i += 1
    
    # get new list without the 1 after multiplier of 5 
    remaining = target - sum(mul5)
    
    if sum(nums) == target:
        return True  
    else:
        non_mul5 = []
        for num in nums:
            if num % 5 != 0:
                non_mul5.append(num)
        
        for num in non_mul5:
            if num == remaining:
                return True 
                
        total = 0
        for num in non_mul5:
            total += num
            if total == remaining:
                return True
            
    return False


start = 0
nums = [9]
target = 0

print(6,group_sum_5(start, nums, target))  