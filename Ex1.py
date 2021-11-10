import pandas as pd
import json

from Elevator import Elevator


def Ex1 (Building:str, Calls:str, Output:str): # <Building.json> <Calls.csv> <output.csv>
    """
    :param Building:
    :param Calls:
    :param Output:
    :return:
    """
    # At first we try to read the files into variables
    try:
        building, calls, output = exporter(Building, Calls, Output) # it will export the relevant files
    except ImportError as err:
        print(err)
    # we want list of elevators
    print (building)
    building_min_floor = building["_minFloor"]
    building_max_floor = building["_maxFloor"]
    elevators = building["_elevators"]
    elev_list = []
    #create a list that contains all the elevators.
    #Extracting the from the elevaors dictionry
    for elev in elevators:
        id = elev["_id"]
        speed = elev["_speed"]
        elev_minFloor = elev["_minFloor"]
        elev_maxFloor = elev["_maxFloor"]
        closeTime = elev["_closeTime"]
        openTime = elev["_openTime"]
        startTime = elev["_startTime"]
        stopTime = elev["_stopTime"]
        x = Elevator(id,speed,elev_minFloor,elev_maxFloor,closeTime,openTime,startTime,stopTime)
        elev_list.append(x)
    print(elev_list)

    def elevator_allocation():
        """
            :param Building:
            :param Calls:
            :param Output:
            :return: the elevator which we send to answer this call
        """

    def time_calc():
        """
            :param Building:
            :param Calls:
            :param Output:
            :return: the time that will take to the elevator to answer and finish the call
        """

    def fill_output(output:pd.DataFrame, elev_num:int, call_num:int) -> None:
        """
            this function gets the output csv and fill the chosen cell with the allocated elevator
            :param output: the csv output
            :param elev_num: the chosen elevator to take the call (from allocted)
            :param call_num: the number of the call which we fill
        """
        output[5][call_num] = elev_num

def exporter(building, calls, output):
        try:
            with open(building, "r") as my_building:
                my_d = json.load(my_building)  # building JSON reading
        except ImportError as err:
            print(err)
        try:
# we can use our calls csv for more quick calculations: the direction of the call and the length of the route
            call_index = ["Name", "Time", "Source", "Destination", "Status", "Allocation"] # column names
# be aware that "Name" & "Status" columns are unnecessary columns
            my_calls = pd.read_csv(calls, names=call_index) # calls csv importing, with col names
            my_calls["Direction"] = my_calls["Source"] < my_calls["Destination"]  # False = down, True = up
            my_calls["Route_Length"] = abs(my_calls["Source"] - my_calls["Destination"])
        except ImportError as err:
            print(err)
        try:
            my_output = pd.read_csv(output, header=None)  # output csv importing, without names
        except ImportError as err:
            print(err)
        return (my_d, my_calls, my_output)
# d1, d2, d3 = exporter("data/Ex1_input/Ex1_Buildings/B1.json","data/Ex1_input/Ex1_Calls/Calls_a.csv","data/Ex1_input/Ex1_Calls/Calls_a.csv")
# print(d1)
# print(d2)
# print(d3)
Ex1("data/Ex1_input/Ex1_Buildings/B1.json","data/Ex1_input/Ex1_Calls/Calls_a.csv","data/Ex1_input/Ex1_Calls/Calls_a.csv")
