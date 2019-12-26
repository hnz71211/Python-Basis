
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

class Solution(object):
    def searchInsert(self, nums, target):
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        if target > nums[-1]:
            return nums_len

        left, right = 0, nums_len - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))