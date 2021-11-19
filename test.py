import unittest

from Elevator import Elevator
from Ex1 import Ex1
import json

class Testing(unittest.TestCase):
    def test_Elevator(self):
        building = \
        {
            "_minFloor": -2,
            "_maxFloor": 10,
            "_elevators": [
                {
                    "_id": 0,
                    "_speed": 0.5,
                    "_minFloor": -2,
                    "_maxFloor": 10,
                    "_closeTime": 2.0,
                    "_openTime": 2.0,
                    "_startTime": 3.0,
                    "_stopTime": 3.0
                }
            ]
        }
        json_dmb = json.dumps(building)
        my_elev = json.loads(json_dmb)
        assert (type(my_elev) is dict)


    #def test_Ex1(self):


if __name__ == '__main__':
    unittest.main()



