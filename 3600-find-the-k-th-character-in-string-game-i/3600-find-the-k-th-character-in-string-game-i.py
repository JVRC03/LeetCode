class Solution:
    def kthCharacter(self, k: int) -> str:
        jvrc = 'a'

        while len(jvrc) < k:
            curr = ''
            for i in range(len(jvrc)):
                if jvrc[i] == 'z':
                    curr += 'a'
                    continue
                curr += chr(ord(jvrc[i])+1)
            jvrc += curr

        return jvrc[k-1]        