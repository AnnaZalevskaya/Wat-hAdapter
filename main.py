from abc import ABC, abstractmethod
import time

class WatchInterface(ABC):
    @abstractmethod
    def viewing_time(self):
        pass

class DigitalWatch(WatchInterface):
    def __init__(self, wtime):
        self.wtime = wtime

    def viewing_time(self):
        print("Current time: " + self.get_time())

    def get_time(self):
        return self.wtime

    def enter_the_time(self, nt):
        self.wtime = nt

class ClockWithHands:
    def __init__(self, wtime):
        self.wtime = wtime
        self.format = "vector"

    def get_time(self):
        return self.wtime

    def enter_the_time(self, nt):
        self.wtime = nt

class TimeAdapter(WatchInterface):
    def __init__(self, ctime):
        self.ctime = ctime

    def turn(self, arrow):
        at = self.ctime.get_time().split(":")
        hnt = int(at[0])
        mnt = int(at[1])
        if (mnt + arrow) >= 60:
            h = int((mnt + arrow) / 60)
            hnt += h
        mnt = (mnt + arrow) % 60
        if hnt > 12:
            hnt %= 12
        if hnt < 10:
            str_hnt = "0" + str(hnt)
        else:
            str_hnt = str(hnt)
        if mnt < 10:
            str_nmt = "0" + str(mnt)
        else:
            str_nmt = str(mnt)
        nt = str_hnt + ":" + str_nmt
        return nt

    def viewing_time(self, arrow):
        rtime = self.turn(arrow)
        self.ctime.enter_the_time(rtime)
        print("Received time: " + rtime)


def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        print("Incorrect time input format...")
        return False

def numCheck(ch):
    try:
        int(ch)
        return True
    except ValueError:
        return False


t = input("Enter the time: ")
while not isTimeFormat(t):
    t = input("Enter the time again: ")
dw = DigitalWatch(t)
cwh = ClockWithHands(t)
cwh_adapter = TimeAdapter(cwh)
while True:
    arrow = input("Enter the number of divisions to rotate: ")
    if arrow == 'x': break
    while not numCheck(arrow) or int(arrow) < 0:
        arrow = input("Enter the number of divisions to rotate again: ")
    cwh_adapter.viewing_time(int(arrow))