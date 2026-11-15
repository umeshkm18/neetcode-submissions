class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            hash1 = {}
            hash2 = {}

            for val in range(len(s)):
                if s[val] in hash1.keys():
                    hash1[s[val]]+=1
                else:
                    hash1[s[val]] = 1

            for val in range(len(t)):
                if t[val] in hash2.keys():
                    hash2[t[val]] += 1
                else:
                    hash2[t[val]] = 1


            if hash1 == hash2:
                return True
            else:
                return False