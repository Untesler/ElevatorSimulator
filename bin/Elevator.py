import time
from random import randrange

class Elevator:
    'This class will collect a status each an elevator'

    __threadName = ""
    __status = True
    __floor = 0
    __min_floor = 0
    __max_floor = 0

    def __init__(self, threadName, min_floor, max_floor):
        self.__threadName = threadName
        self.__min_floor = min_floor
        self.__max_floor = max_floor
        return self

    def getName(self):
        return self.__threadName

    def setFloor(self, floor):
        self.__floor = floor

    def getFloor(self):
        return self.__floor

    def printTime(self):
        return "{} || {} || at floor : {}".format(self.__threadName, time.ctime(time.time()), self.__floor)

    def getStart(self):
        return ">Start {} ".format(self.__threadName)

    def letDecide(self):
        flag = False
        if(randrange(1, 9) < 2): flag = True
        return flag

    def cal(self):
        return self.__floor ** 2

