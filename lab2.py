'''
Kyle Krstulich
9/17/24
Physics Lab 1

helper functions for my physics lab.

I know this code is disgusting. I will fix it later I hope.
'''
import pandas as pd
import numpy as np

st = 0.00001
sh = 0.1


test_d = [(1.5, 0.1)]
test_t = [(0.0058, st), (0.0061, st), (0.008, st), (0.0091, st), (0.0178, st)]
test_h = [(46.5, sh), (42, sh), (27.4, sh), (22.9, sh), (12, sh)]

# Convert lists into DataFrame
df_d = pd.DataFrame(test_d, columns=['Distance(cm)', 'Error_D(cm)'])
df_t = pd.DataFrame(test_t, columns=['Time(s)', 'Error_T(s)'])
df_h = pd.DataFrame(test_h, columns=['Height(cm)', 'Error_H(cm)'])
df_g = pd.DataFrame(columns=["Error_g(cm/s)"])

# Combine into one DataFrame (optional)
df_combined = pd.concat([df_d, df_t, df_h, df_g], axis=1)

g = ((1/2) * 1.5**2 * 0.0054**-2 * 42.5**-1)


def deltaG():

    d = (df_combined["Distance(cm)"][0], df_combined["Error_D(cm)"][0])

    for i in range(len(df_combined)):

        t = (df_combined["Time(s)"][i], df_combined["Error_T(s)"][i])
        h = (df_combined["Height(cm)"][i], df_combined["Error_H(cm)"][i])

        sg = g * ((2 * (d[1]/d[0]))**2 * (-2 * (t[1]/t[0]))
                  ** 2 * (-1 * (h[1]/h[0]))**2)**(1/2)

        df_combined.loc[i, "Error_g(cm/s)"] = sg
        print(h)
        print(sg)


def main():
    deltaG()
    print(df_combined)


if __name__ == "__main__":
    main()
