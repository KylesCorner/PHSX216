"""
Kyle Krstulich
10/1/24
lab3.py

Helper functions for my lab...

"""
import pandas as pd
import numpy as np


def stdUncMean(data):

    # Calculate the standard deviation
    std_dev = np.std(data, ddof=1)  # Use ddof=1 for sample standard deviation

    # Calculate the standard uncertainty in the mean
    std_uncertainty = std_dev / np.sqrt(len(data))

    return std_uncertainty


def delta_V_o(df):
    v_o = df["v_o"]
    d = (df["dDeltad"]/df["deltad"])**2
    dDeltat_avg = stdUncMean(df["Deltat"])
    t = (dDeltat_avg/df["deltat"])**2
    output = v_o * (d + t)**(1/2)

    return output


def main():
    df = pd.read_csv("lab3.csv")
    dDeltat_avg = stdUncMean(df["Deltat"])
    deltavprime = delta_V_o(df)
    test = []
    for i in range(5):
        x = df.iloc[:, i]
        test.append(stdUncMean(x))
    dy_avg = pd.Series(test)
    df["deltav_o"] = deltavprime
    df["deltay_avg"] = dy_avg

    print(df)


if __name__ == "__main__":
    main()
