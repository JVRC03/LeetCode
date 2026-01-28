class Solution:
    def greatestLetter(self, s: str) -> str:
        st = set()
        arr = list(s)
        arr.sort(reverse = True)

        jvrc = ''
        
        for i in range(len(arr)):
            if arr[i].islower():
                st.add(arr[i])
            else:
                temp = arr[i].lower()

                if temp in st:
                    jvrc = max(jvrc, arr[i])
        
        return jvrc
        