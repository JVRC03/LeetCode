class AuthenticationManager:

    def __init__(self, e: int):
        self.k = e
        self.dic = {}
        
    def generate(self, i: str, c: int) -> None:
        self.dic[i] = c

    def renew(self, i: str, c: int) -> None:
        if i not in self.dic:
            return None

        if c >= self.dic[i]+self.k:
            return None
        
        self.dic[i] = c

    def countUnexpiredTokens(self, c: int) -> int:
        jvrc = 0

        for i in self.dic:
            if self.dic[i]+self.k > c:
                jvrc += 1
                
        return jvrc
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)