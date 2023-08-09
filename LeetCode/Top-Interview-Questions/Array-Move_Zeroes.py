class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        i = 0
        l = len(nums)
        if len(nums) >= 2:
            while i < l:
                if nums[i] == 0:
                    del nums[i]
                    nums.append(0)
                    l -= 1
                else:
                    i += 1