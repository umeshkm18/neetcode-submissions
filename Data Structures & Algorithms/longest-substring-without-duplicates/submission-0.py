class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            st = set()
            l = 0
            r = 0
            mx_length = 0
            curr_length = 0
            for r in range(len(s)):
                while s[r] in st :
                    st.remove(s[l])
                    l+=1
                st.add(s[r])

                curr_length = r-l+1

                mx_length = max(mx_length,curr_length)

            return mx_length