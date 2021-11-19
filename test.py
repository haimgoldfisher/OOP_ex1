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
        my_building = json.loads(json_dmb)
        my_elev = my_building["_elevators"][0]
        self.assertTrue(type(my_elev) is dict)
        self.assertEqual(my_elev["_id"], 0)
        self.assertEqual(my_elev["_speed"], 0.5)
        self.assertEqual(my_elev["_minFloor"], -2)
        self.assertEqual(my_elev["_maxFloor"], 10)
        self.assertEqual(my_elev["_closeTime"], 2.0)
        self.assertEqual(my_elev["_openTime"], 2.0)
        self.assertEqual(my_elev["_startTime"], 3.0)
        self.assertEqual(my_elev["_stopTime"], 3.0)

        elev = Elevator(my_elev)
        self.assertTrue(type(my_elev) is dict)
        self.assertEqual(elev.id, 0)
        self.assertEqual(elev.speed, 0.5)
        self.assertEqual(elev.minFloor, -2)
        self.assertEqual(elev.maxFloor, 10)
        self.assertEqual(elev.closeTime, 2.0)
        self.assertEqual(elev.openTime, 2.0)
        self.assertEqual(elev.startTime, 3.0)
        self.assertEqual(elev.stopTime, 3.0)

    def test_Ex1(self):
        building, calls, output = exporter("B1.json", "Calls_a.csv", "Calls_a.csv")
        for i in range(len(calls)):
            if calls.iloc[i].Source < calls.iloc[i].Destination:
                self.assertTrue(calls.iloc[i]["Direction"])
            else:
                self.assertFalse(calls.iloc[i]["Direction"])



if __name__ == '__main__':
    unittest.main()


