class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hash1 = {} # {1:1,2:2,3:3}
            for num in nums:
                hash1[num] = 1+hash1.get(num,0)
            res = dict(sorted(hash1.items(),key=lambda item:item[1],reverse=True))
        
            return list(res.keys())[:k]