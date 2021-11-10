class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime) -> None:
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.calls = []

    def __init__(self, elevator) -> None:
        self.id = elevator["_id"]
        self.speed = elevator["_speed"]
        self.minFloor = elevator["_minFloor"]
        self.maxFloor = elevator["_maxFloor"]
        self.closeTime = elevator["_closeTime"]
        self.openTime = elevator["_openTime"]
        self.startTime = elevator["_startTime"]
        self.stopTime = elevator["_stopTime"]
        self.calls = []

    def __str__(self) -> str:
        return f"id:{self.id}, speed:{self.speed}, minFloor:{self.minFloor}, maxFloor:{self.maxFloor}, closeTime:{self.closeTime}," \
               f" openTime:{self.openTime}, startTime:{self.startTime}, stopTime:{self.stopTime}"

    def __repr__(self) -> str:
        return self.__str__()



# x = Elevator(0,0.5,-2,10,2,2,3,3)
# print(x)
# print(x.speed)
