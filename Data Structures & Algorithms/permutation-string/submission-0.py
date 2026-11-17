class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                s1count = Counter(s1)
                l = 0
                r = 0
                s2count ={}

                # return s1count.total()

                for r in range(len(s2)):
                        # s2count = Counter(s2[r])
                        s2count[s2[r]] = 1+ s2count.get(s2[r],0)
                        if r-l+1 == s1count.total():
                                
                                
                                if s1count == s2count:
                                        return True
                                
                                s2count[s2[l]]-=1
                                
                                if s2count[s2[l]]==0:
                                        del s2count[s2[l]]

                                l+=1
                return False