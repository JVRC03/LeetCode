class Solution:
    def numberOfRounds(self, lit: str, lot: str) -> int:
        st = (int(lit[0:2])*60) + (int(lit[3:len(lit)]))
        end = (int(lot[0:2])*60) + (int(lot[3:len(lot)]))

        jvrc = 0
        if st <= end:
            temp = st%15
            if temp!=0:
                st += (15-temp)
            while (st+15) <= end:
                st += 15
                jvrc += 1
        else:
            temp = st%15
            if temp!=0:
                st += (15-temp)
            while (st+15) <= 1440:
                st += 15
                jvrc += 1
            st = 0
            while (st+15) <= end:
                st += 15
                jvrc += 1
        
        return jvrc

        