class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        l = len(nums)

        while i < l-1:
            if nums[i] != nums[i+1]:
                k += 1
                i += 1
            else:
                del nums[i]
                l -= 1
        k += 1
        
        return k