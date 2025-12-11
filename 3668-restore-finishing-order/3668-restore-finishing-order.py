class Solution:
    def recoverOrder(self, arr: List[int], jvrc: List[int]) -> List[int]:
        k = set(jvrc)
        jvrc = []
        for i in range(len(arr)):
            if arr[i] in k:
                jvrc.append(arr[i])
        
        return jvrc
