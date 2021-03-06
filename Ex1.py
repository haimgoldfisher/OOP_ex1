import pandas as pd
import json

from Elevator import Elevator
import sys


def Ex1(Building: str, Calls: str, Output: str):  # <Building.json> <Calls.csv> <output.csv>
    """
    :param Building: address of the building json file
    :param Calls: address of the calls csv
    :param Output: address of the calls csv
    The main function of the program, it will insert the allocating column of the calls csv (output csv)
    """
    # At first we try to read the files into variables
    try:
        building, calls, output = exporter(Building, Calls, Output)  # it will export the relevant files
    except ImportError as err:
        print(err)
    print(building)
    building_min_floor = building["_minFloor"]
    building_max_floor = building["_maxFloor"]
    elevators = building["_elevators"]
    elev_list = []  # a want list of elevators
    # create a list that contains all the elevators.
    # Extracting the data from the elevators dictionary
    for elev in elevators:
        x = Elevator(elev)
        elev_list.append(x)
    print(elev_list)
    print(calls)
    for call in range(len(calls)):
        elev_id = elevator_allocation(elev_list, calls.iloc[call])
        # fill_output(output, elev_id, call)
        output.loc[call, "Allocation"] = elev_id
    print(output)
    output.to_csv('output', header=False, index=False)


def elevator_allocation(elev_list: list, call: int) -> int:
    """
        :param elev_list: the list of the elevators of the building
        :param call: the index of the call in the Calls data frame (pandas)
        :return: the elevator's index which we send to answer this call
        this function will go over the elevator and for each one it will calculate the time will ut to
        answer the new call. finally it will return the id of the elevator that will answer the call in
        the lowest time.
    """
    min_time = float('inf')
    elev_id = -1
    for elev in elev_list:
        curr_time = time_calc(elev, call)
        if curr_time < min_time:
            min_time = curr_time
            elev_id = elev.id
    elev_list[elev_id].calls.append(call)
    elev_id
    return elev_id


def time_calc(elev: Elevator, call: int) -> float:
    """
        :param elev: the chosen elevator which we want to calculate it's time to answer and finish the given call
        :param call: the index of the call in the Calls data frame (pandas)
        :return: the time that will take to the elevator to answer and finish the call
        for a given elevator this function will calculate its current rout and the time it will take it
        to answer a given call.
    """
    time_per_floor = 1 / elev.speed
    num_calls = len(elev.calls)
    if num_calls == 0:
        return 0
    rout = [elev.calls[0].Source]
    max_min = elev.calls[0].Destination
    for i in range(num_calls - 1):
        curr_type = elev.calls[i].Direction
        next_type = elev.calls[i + 1].Direction
        if next_type == curr_type:
            if curr_type == True:
                max_min = max(max_min, elev.calls[i + 1].Destination)
            else:
                max_min = min(max_min, elev.calls[i + 1].Destination)
        if next_type != curr_type:
            if curr_type == True:
                max_min = max(max_min, elev.calls[i + 1].Source)
            else:
                max_min = min(max_min, elev.calls[i + 1].Source)
            rout.append(max_min)
            max_min = elev.calls[i + 1].Destination
        if i + 1 == num_calls and next_type == curr_type:
            rout.append(max_min)
    floors_passing = 0
    for i in range(len(rout) - 1):
        x = rout[i]
        y = rout[i + 1]
        floors_passing += abs(x - y)
    rout_time = floors_passing * time_per_floor + num_calls * (
                elev.startTime + elev.stopTime + elev.openTime + elev.closeTime)
    return rout_time


def fill_output(output: pd.DataFrame, elev_num: int, call_num: int) -> None:
    """
        this function gets the output csv and fill the chosen cell with the allocated elevator
        :param output: the csv output
        :param elev_num: the chosen elevator to take the call (from allocted)
        :param call_num: the number of the call which we fill
    """
    output.loc[call_num]["Allocation"] = elev_num


def exporter(building: str, calls: str, output: str):
    try:
        with open(building, "r") as my_building:
            my_d = json.load(my_building)  # building JSON reading
    except FileExistsError as err:
        print(err)
    finally:
        my_building.close()
    try:
        # we can use our calls csv for more quick calculations: the direction of the call and the length of the route
        call_index = ["Name", "Time", "Source", "Destination", "Status", "Allocation"]  # column names
        # be aware that "Name" & "Status" columns are unnecessary columns
        my_calls = pd.read_csv(calls, names=call_index)  # calls csv importing, with col names
        my_calls["Direction"] = my_calls["Source"] < my_calls["Destination"]  # False = down, True = up
        my_calls["Route_Length"] = abs(my_calls["Source"] - my_calls["Destination"])
    except ImportError as err:
        print(err)
    try:
        my_output_index = ["Name", "Time", "Source", "Destination", "Status", "Allocation"]  # column names
        my_output = pd.read_csv(output, names=my_output_index)  # calls csv importing, with col names
        my_output["Direction"] = my_output["Source"] < my_output["Destination"]  # False = down, True = up
        my_output["Route_Length"] = abs(my_output["Source"] - my_output["Destination"])
    except ImportError as err:
        print(err)
    return (my_d, my_calls, my_output)


if len(sys.argv) == 4:
    Ex1(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    Ex1("B1.json", "Calls_a.csv", "Calls_a.csv")