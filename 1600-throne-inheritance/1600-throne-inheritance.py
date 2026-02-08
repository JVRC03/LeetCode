class ThroneInheritance:

    def __init__(self, king: str):
        self.dic = {king : []}
        self.main = king
        self.s = set()

    def birth(self, parent: str, child: str) -> None:
        if parent not in self.dic:
            self.dic[parent] = [child]
        else:
            self.dic[parent].append(child)

    def death(self, name: str) -> None:
        self.s.add(name)

    def getInheritanceOrder(self) -> List[str]:
        jvrc = []

        def dfs(root):
            if root not in self.s:
                jvrc.append(root)
            
            if root not in self.dic:
                return

            arr = self.dic[root]

            for i in range(len(arr)):
                dfs(arr[i])

        dfs(self.main)

        return jvrc
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()