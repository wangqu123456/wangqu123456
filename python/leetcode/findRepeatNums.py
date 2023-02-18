def findRepeatNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    all_nums = set()
    print(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            all_nums.add(nums[i])
    return all_nums

def findRepeatNumber(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
            elif nums[i] == nums[j]:
                return nums[i]
        if i > 1 and (nums[i] - nums[i - 1]) != 1:
            return nums

mylist=[2, 3, 1, 0, 2, 5, 3]
print(findRepeatNumber(mylist))
