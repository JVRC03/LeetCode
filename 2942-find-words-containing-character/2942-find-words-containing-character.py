class Solution:
    def findWordsContaining(self, arr: List[str], x: str) -> List[int]:
        jvrc = []

        for i in range(len(arr)):
            if x in arr[i]:
                jvrc.append(i)
        
        return jvrc

        