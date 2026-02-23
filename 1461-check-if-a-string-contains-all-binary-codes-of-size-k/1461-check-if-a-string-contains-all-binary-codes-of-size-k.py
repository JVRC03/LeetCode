class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()

        for i in range(len(s)):
            if i + k > len(s):
                break
            
            temp = s[i:i+k]

            st.add(temp)

        if len(st) != int(math.pow(2, k)):
            return False
        
        return True
        