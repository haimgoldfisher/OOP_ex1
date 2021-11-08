import pandas as pd
import json

def Ex1 (Building:str, Calls:str, Output:str): # <Building.json> <Calls.csv> <output.csv>
    try:
        building, calls, output = exporter(Building, Calls, Output) # it will export the relevant files
    except ImportError as err:
        print(err)
    # we want list of elevators







def exporter(Building, Calls, output):
        try:
            with open(Building, "w") as my_building:
                json.dumps(str, fp=my_building)  # building JSON importing
        except ImportError as err:
            print(err)
        try:
            my_calls = pd.read_csv(Calls)  # calls csv importing
        except ImportError as err:
            print(err)
        try:
            my_output = pd.read_csv(output)  # output csv importing
        except ImportError as err:
            print(err)
        return (my_building, my_calls, my_output)