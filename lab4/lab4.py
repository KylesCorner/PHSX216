"""
Kyle Krstulich
10/2/24
Physics 1
lab4.py



"""

import pandas as pd
import numpy as np
import math

# Constants
g = 9.81


df_ids_g_to_kg = [
    'M',
    'deltaM',
    'm',
    'deltam',
]

df_ids_cm_to_m = [
    'r_1',
    'r_2',
    'r_3',
    'r_4',
    'r_5',
    'deltar',
]

df_ids_time = [
    't_1',
    't_2',
    't_3',
    't_4',
    't_5'
]

# dataframe
data = pd.read_csv("lab4data.csv")


def _grams_to_kilograms(input_series):
    return input_series.div(1000)


def _centemeter_to_meter(input_series):
    return input_series.div(100)


def _clean_data():

    # Unit conversion
    for s in data:
        if s in df_ids_g_to_kg:
            data[s] = _grams_to_kilograms(data[s])
        if s in df_ids_cm_to_m:
            data[s] = _centemeter_to_meter(data[s])


_clean_data()


def stdUncMean(id):

    # Calculate the standard deviation
    # Use ddof=1 for sample standard deviation
    std_dev = np.std(data[id], ddof=1)

    # Calculate the standard uncertainty in the mean
    std_uncertainty = std_dev / np.sqrt(len(data[id]))

    return std_uncertainty


def power_product(test_id: str, a_tup: tuple, b_id: str):
    a, deltaa = a_tup
    b = data[b_id]
    deltab = data["delta"+b_id]
    test = data[test_id]

    decrim_a = (deltaa/a)**2
    decrim_b = (deltab/b)**2

    output = test * (decrim_a + decrim_b)**(1/2)

    sr = pd.Series(output)
    return sr


def partOne():

    hex_weight = data["M"]
    cylinder_weight = data["m"]

    # Calculate Force of tension
    # also the net centeripetal force
    data["F_t"] = g * hex_weight
    # find error in calculation
    data["deltaF_t"] = power_product("F_t", (g, 0.01), "M")


def partTwo():

    # Calclulate average time invervals
    data["t_avg"] = 0
    for id in df_ids_time:
        data["t_avg"] += data[id]
    data["t_avg"] = data["t_avg"]/len(df_ids_time)

    # calculate error in average time calculations
    data["deltat_avg"] = 0
    for n, id in enumerate(df_ids_time):
        data.loc[n, "deltat_avg"] = stdUncMean(id)

    # calculate T
    data["T"] = 0
    for e in data["t_avg"]:
        data["T"] += data["t_avg"]/5

    data["F_c"] = 0
    for n, e in enumerate(data["T"]):
        data.loc[n, "F_c"] = 2*math.pi*data["m"][0]/e


def main():
    partOne()
    partTwo()
    print(data)


if __name__ == "__main__":
    main()
