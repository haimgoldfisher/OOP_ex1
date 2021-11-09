import pandas as pd
import json

def Ex1 (Building:str, Calls:str, Output:str): # <Building.json> <Calls.csv> <output.csv>
    try:
        building, calls, output = exporter(Building, Calls, Output) # it will export the relevant files
    except ImportError as err:
        print(err)
    # we want list of elevators


def exporter(building, calls, output):
        try:
            with open(building, "r") as my_building:
                my_d = json.load(my_building)  # building JSON reading
        except ImportError as err:
            print(err)
        try:
            my_calls = pd.read_csv(calls)  # calls csv importing
        except ImportError as err:
            print(err)
        try:
            my_output = pd.read_csv(output)  # output csv importing
        except ImportError as err:
            print(err)
        return (my_d, my_calls, my_output)
d1, d2, d3 = exporter("data/Ex1_input/Ex1_Buildings/B1.json","data/Ex1_input/Ex1_Calls/Calls_a.csv","data/Ex1_input/Ex1_Calls/Calls_a.csv")
print(d1)
print(d2)
print(d3)
