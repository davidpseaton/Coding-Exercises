class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()

        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        else:
            if nums[0] != 0:
                return 0
            for i in range(0,len(nums)):
                if i == len(nums)-1:
                    return nums[i]+1
                else:
                    if nums[i+1]-nums[i] == 1:
                        continue
                    else:
                        return nums[i]+1
						
						
#Other Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        for i in range(len(nums)):
            if new_nums[i] != i:
                return i
        return len(nums)
		
		
#Fastest Solution
class Solution:
    def missingNumber(self, nums):
      n = len(nums)
      return int(n * (n+1) / 2 - sum(nums))