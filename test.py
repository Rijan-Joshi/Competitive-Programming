def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(nums) - 1
    a = []

    while (l <= r):
        mid = (l + r) // 2
        print(mid)

        if nums[mid] == target:
            a.append(mid)
        
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        
    if len(a) == 0:
        return [-1,-1]
    else:
        return a

print(searchRange([5,7,7,8,8,10], 8))
