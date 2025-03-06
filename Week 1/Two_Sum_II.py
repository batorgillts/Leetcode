class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
                
print(Solution().twoSum([2,7,11,15], 9)) # [1,2]
print(Solution().twoSum([2,3,4], 6)) # [1,3]
print(Solution().twoSum([-1,0], -1)) # [1,2]
