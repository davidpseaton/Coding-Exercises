class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        flag = False
        
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1] and len(nums) >= 2:
                flag = True
                break;
                
        return flag