import json


class Elevator(object):
    def __init__(self, id: str, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float,
                 startTime: float, stopTime: float, **kwargs) -> None:
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

    def load_from_jfile(self, file_name: str):
        new_elev_dict = {}
        try:
            with open(file_name, "r") as file:
                dict_obj = json(file)
                for i, j in dict_obj.items():
                    elev = Elevator(**j)
                    new_elev_dict[i] = elev
                self.calls = new_elev_dict
        except FileExistsError as err:
            print(err)

    def __str__(self) -> str:
        return f"id:{self.id}, speed:{self.speed}, minFloor:{self.minFloor}, maxFloor:{self.maxFloor}, closeTime:{self.closeTime}," \
               f" openTime:{self.openTime}, startTime:{self.startTime}, stopTime:{self.stopTime}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self) -> json:
        my_dict = self.__dict__
        return json.dumps(my_dict)
