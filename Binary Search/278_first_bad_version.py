 def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """

    left = 1
    right = n

    while left <= right:
        mid = left + ((right - left) / 2)
        if(isBadVersion(mid)): 
            right = mid
        else:
            left = mid + 1
            
    if left == right and isBadVersion(left):
        return left

    return -1


firstBadVersion(349)