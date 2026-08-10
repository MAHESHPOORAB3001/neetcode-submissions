class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        nums.sort()  
        
        for i in range(0, len(nums)):
            print(nums[i]) 
            
        return nums

       
            