
class ElevatorHandler:

    __instance = None
    __user = ""
    __passenger_queue = dict() 
    __max_floor = 8
    __nElevator = 0

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ElevatorHandler.__instance == None:
            ElevatorHandler.__instance = ElevatorHandler
        return ElevatorHandler.__instance

    @staticmethod
    def setUser(msg):
        ElevatorHandler.__User = msg
        return ElevatorHandler.__instance
    
    @staticmethod
    def setNElevator(n):
        ElevatorHandler.__nElevator = n
        return ElevatorHandler.__instance

    @staticmethod
    def setMaxFloor(max):
        ElevatorHandler.__max_floor = max
        return ElevatorHandler.__instance
    
    @staticmethod
    def getMaxFloor():
        return ElevatorHandler.__max_floor
    
    @staticmethod
    def getUser():
        return ElevatorHandler.__User
    
    @staticmethod
    def initPassengerQueue(nFloor):
        for i in range(1, nFloor + 1):
            ElevatorHandler.__passenger_queue.update({i : 0})
        return ElevatorHandler.__instance
    
    @staticmethod
    def enqueue(intratenant):
        if len(ElevatorHandler.__passenger_queue) == 0:
            raise Exception("passenger_queue is empty.")
        for i in range(1, len(intratenant) + 1):
            ElevatorHandler.__passenger_queue[i] += intratenant[i]
        return ElevatorHandler.__instance

    @staticmethod
    def dequeue(currentFloor, isUp, elevatorID, size):
        """ Decide to let an elevator dequeue or not """
        meanFloor = ElevatorHandler.__nElevator - ElevatorHandler.__nElevator//2
        if meanFloor < elevatorID:
            #high floor
            if(isUp):
                for i in range(currentFloor, ElevatorHandler.__max_floor + 1):
                    pass
            else:
                for i in range(currentFloor, 0, -1):
                    if i != 1 and i < meanFloor: continue
                    pass
        else:
            #low floor
            if(isUp):
                for i in range(currentFloor, meanFloor + 1):
                    pass
            else:
                for i in range(currentFloor, 0, -1):
                    pass
        return

    def __init__(self):
        """ Virtually private constructor """
        if ElevatorHandler.__instance != None:
            ElevatorHandler.__instance = None
        raise Exception("Can't instantiate a singleton class.")

if __name__ == "__main__":
    e = ElevatorHandler.getInstance()
    f = ElevatorHandler.getInstance()
    e.setUser('E')
    f.setUser('X')
    print(e.getUser())
    print(f.getUser())