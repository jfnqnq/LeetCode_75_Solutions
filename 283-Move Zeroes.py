#283-Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0,0
        while left < len(nums) and right < len(nums):
            if nums[left] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            left +=1
