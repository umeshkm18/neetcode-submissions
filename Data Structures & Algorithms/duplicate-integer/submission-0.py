class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data_set = set()
        for num in nums:
            if num in data_set:
                return True
            else:
                data_set.add(num)
        return False

