import json

class Elevator(object):
    def __init__(self, id: str, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float, startTime: float, stopTime: float) -> None:
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

    def __lt__(self, other) -> bool:
        # should compare between time attributes of two elevators
        # RETURN self.TIME? < other.TIME? -- we should use here time_calc method
        pass

    # def to_dict(self) -> dict:
    #     return self.__dict__

    def to_json(self) -> json:
        my_dict = self.__dict__
        return json.dumps(my_dict)
# x = Elevator(0,0.5,-2,10,2,2,3,3)
# print(x)
# print(x.speed)
