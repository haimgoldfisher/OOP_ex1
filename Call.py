import json


class Call(object):
    def __int__(self, time: float, source: int, dest: int) -> None:
        self.name = "Elevator call"
        self.time = time
        self.source = source
        self.dest = dest
        self.status = -1
        self.allocating = -1

    def __str__(self) -> str:
        return f"name:{self.name}, time:{self.time}, source:{self.source}, dest:{self.dest}, status:{self.status}," \
               f"allocating:{self.allocating}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self) -> json:
        my_dict = self.__dict__
        return json.dumps(my_dict)

