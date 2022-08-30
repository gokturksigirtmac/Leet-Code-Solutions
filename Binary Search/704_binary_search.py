nums = [-1,0,3,5,9,12]
target = 12

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = int((left + right) / 2)
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            
        return -1

search(nums, target)