class Solution:
    def __init__(self):
        self.jvrc = set()

    def back_track(self, arr, k, temp):

        if len(temp) == k:
            hrs, mins = 0, 0
            for i in range(len(temp)):
                if temp[i] <= 3:
                    hrs += arr[temp[i]]
                else:
                    mins += arr[temp[i]]
            
            if hrs > 11 or mins > 59:
                return 
            
            temp = ''
            if mins < 10:
                temp = '0'
            s = str(hrs) + ':' + (temp+str(mins))

            self.jvrc.add(s)
            return

        for i in range(len(arr)):
            if i not in temp:
                temp.append(i)
                self.back_track(arr, k, temp)
                temp.pop()

    def readBinaryWatch(self, k: int) -> List[str]:
        arr = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]

        self.back_track(arr, k, [])

        return list(self.jvrc)
        