import unittest

from Elevator import Elevator
from Ex1 import Ex1, time_calc, elevator_allocation, exporter
import json
import pandas as pd

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
        self.assertTrue(type(my_elev) is dict)
        self.assertEqual(my_elev["_speed"], 0.5)

        elev_dct = Elevator("1", 1, 2, 3, 4, 5, 6, 7)
        self.assertNotEqual(elev_dct["_speed"], elev_dct["_stopTime"])

    def test_Ex1(self):
        building, calls, output = exporter("B1.json", "Calls_a.csv", "Calls_a.csv")
        for i in range(len(calls)):
            if calls[i]["Source"] > calls[i]["Destination"]:
                self.assertTrue(calls[i]["Direction"])
            else:
                self.assertFalse(calls[i]["Direction"])


if __name__ == '__main__':
    unittest.main()


