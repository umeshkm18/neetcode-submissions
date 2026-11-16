class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        mxvalue = -9999
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            mxvalue = max(mxvalue,prices[r]-prices[l])
        return max(mxvalue,0)