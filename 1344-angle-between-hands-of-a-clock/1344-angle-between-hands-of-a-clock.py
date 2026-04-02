class Solution:
    def angleClock(self, hour: int, mins: int) -> float:
        # 1hr = 6 degrees
        # 1min = 1/2 degree (hour hand)

        if hour == 12:
            hour = 0

        hr = (hour * 30) + (mins * 0.5)

        mini = mins * 6

        jvrc = abs(hr - mini)

        if jvrc > 180:
            jvrc = abs(360 - jvrc)

        return jvrc



        