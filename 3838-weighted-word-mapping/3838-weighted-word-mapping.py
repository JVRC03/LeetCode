class Solution:
    def mapWordWeights(self, s: List[str], arr: List[int]) -> str:
        jvrc = ''

        for i in range(len(s)):
            curr, temp = 0, s[i]

            for j in range(len(temp)):
                curr += arr[ord(temp[j]) % 97]
            
            val = curr % 26
            jvrc += chr(122 - val)
        
        return jvrc
            

        