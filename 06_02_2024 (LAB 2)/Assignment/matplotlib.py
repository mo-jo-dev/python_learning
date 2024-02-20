import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('city_temperature.csv')

print("DataFrame:")
print(df)
print("\nDataFrame Shape:")
print(df.shape)

x_line = df['Column1']
y_line = df['Column3']

plt.plot(x_line, y_line)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()

plt.scatter(df['Column1'], df['Column2'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot using Matplotlib')
plt.show()
