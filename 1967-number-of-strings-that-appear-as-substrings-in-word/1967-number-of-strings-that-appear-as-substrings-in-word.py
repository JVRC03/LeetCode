class Solution:
    def numOfStrings(self, arr: List[str], word: str) -> int:
        jvrc = 0

        for i in range(len(arr)):
            if arr[i] in word:
                jvrc += 1
        
        return jvrc
        