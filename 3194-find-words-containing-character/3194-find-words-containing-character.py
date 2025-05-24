class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        jvrc = []

        for i in range(len(words)):
            if x in words[i]:
                jvrc.append(i)
        
        return jvrc
        