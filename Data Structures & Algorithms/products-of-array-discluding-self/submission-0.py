class Solution:
    def productExceptSelf(self, nums: List[int]):
            left = [1]*len(nums)
            right = [1]*len(nums)
            res = [1]*len(nums)

            for n in range(1,len(nums)):
                left[n] = nums[n-1]*left[n-1]
            
            for n in range(len(nums)-2,-1,-1):
                right[n] = nums[n+1]* right[n+1]
            
            
            for i in range(len(nums)):
                res[i] = left[i]*right[i]
            return res
