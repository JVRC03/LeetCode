class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        small, big = [0] * 26, [0] * 26
        no = set()
        
        for i in range(len(s)):
            val = ord(s[i])

            idx = -1
            if s[i].islower():
                idx = val % 97
                small[idx] += 1
            else:
                idx = val % 65
                big[idx] += 1
            
            if big[idx] and s[i].islower():
                no.add(s[i])

        jvrc = 0
        for i in range(26):
            if chr(97 + i) in no:
                continue

            if big[i] > 0 and small[i] != 0:
                jvrc += 1
                
        return jvrc

            



            

    
        return jvrc
        