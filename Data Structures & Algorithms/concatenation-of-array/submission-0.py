class Solution:
    def getConcatenation(self, nums: List[int]):
        # length = len(nums)*2
        new_nums = []
        for num in range(len(nums)):
            new_nums.append(nums[num])

        for num in range(len(nums)):
            new_nums.append(nums[num])
        
        return new_nums
