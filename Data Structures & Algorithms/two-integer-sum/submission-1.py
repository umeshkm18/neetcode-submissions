class Solution:
    def twoSum(self, nums: List[int], target: int):
        h_key = {num:i for i,num in enumerate(nums)}
        for num in range(len(nums)):
            bal = target - nums[num]
            if bal in h_key and h_key[bal] != num:
                return [num, h_key.get(bal)]