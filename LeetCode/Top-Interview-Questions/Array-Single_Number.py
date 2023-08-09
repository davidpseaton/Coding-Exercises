class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        tempSearch = 0
        tempNums = []
        
        for i in range(0,len(nums)):
            tempNums = nums[:]
            tempSearch = nums[i]
            del tempNums[i]
            if nums[i] not in tempNums:
                return nums[i]
                
        return 0

#Faster solution (originally was going to use a Dict like this,
#but because I hadn't coded the 2nd for-loop yet, an error kept
#spitting out about "no return value" so I changed my approach.)		
		
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        for num, count in num_counts.items():
            if count == 1:
                return num