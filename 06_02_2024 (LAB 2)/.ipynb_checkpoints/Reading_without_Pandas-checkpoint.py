import pandas as pd
import numpy as npy
path = 'salaries.csv'

def load_csv(path):
    data = []
    col = []
    check = False
    with open(path) as f:
        for val in f.readlines():
            val = val.replace("\n", "")
            val = val.split(",")
            if not check:
                col = val
                check = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns = col)
    return df


load_df = load_csv(path)
print(load_df)


# data = npy.loadtxt(path, delimiter = ',', dtype = str)
# print(data[5,:])
    
# data = npy.genfromtxt(path, delimiter = ',')
# pd.DataFrame(data)