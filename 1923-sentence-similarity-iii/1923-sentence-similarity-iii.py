class Solution:
    def areSentencesSimilar(self, a: str, b: str) -> bool:
        a = a.split(' ')
        b = b.split(' ')

        while len(a) and len(b) and a[-1] == b[-1]:
            a.pop()
            b.pop()
        
        a = a[::-1]
        b = b[::-1]

        while len(a) and len(b) and a[-1] == b[-1]:
            a.pop()
            b.pop()
        
        if not len(a) or not len(b):
            return True
        
        return False
        

        