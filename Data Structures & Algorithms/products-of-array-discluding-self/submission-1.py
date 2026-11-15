class Solution:
    def productExceptSelf(self, nums: List[int]):
                    left = [1]*len(nums)
                    res = [1]*len(nums)

                    for n in range(1,len(nums)):
                        left[n] = nums[n-1]*left[n-1]
                    pos =1
                    for n in range(len(nums)-2,-1,-1):
                        # pos = nums[n+1]*pos
                        # res[n] = pos * left[n]       1 2 3 4
                        res[n+1] = pos * left[n+1]  # [1,1,1,1*8]
                        pos = nums[n+1]*pos # pos = 6*1 this is my right
                    res[0] = pos
                    return res

                    