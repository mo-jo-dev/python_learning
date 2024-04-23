import pandas as pd

data = {
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E'],
    'Column3': [10.5, 20.3, 15.8, 7.2, 11.0],
    'Column4': ['X', 'Y', 'Z', 'W', 'U'],
    'Column5': [True, False, True, False, True]
}

df = pd.DataFrame(data)

df.to_csv('sample.csv', index=False)