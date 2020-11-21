import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([12.93014,
              6.65058,
              9.62082,
              53.93707,
              18.22959,
              7.48008,
              13.73508,
              20.94819,
              46.72332,
              24.24886,
              14.50726,
              3.92171,
              27.62664,
              1.89725,
              8.16686,
              2.36952,
              1.81861,
              61.71342,
              38.86611,
              41.20003,
              41.95896,
              9.24151,
              26.49084,
              71.69556,
              28.11535,
              14.524,
              6.85889,
              1.41849,
              1.01286,
              12.97168,
              8.34033,
              26.63188,
              13.43828,
              11.78272,
              4.88026,
              51.87869,
              6.32161,
              73.13787,
              4.09012,
              2.82573])
y = np.array([78.33,
              60.38,
              74.8,
              81.64,
              78.98,
              70.95,
              77.13,
              74.81,
              81.95,
              79.91,
              76.93,
              57.02,
              78.02,
              65.87,
              73.81,
              60.71,
              63.29,
              84.68,
              82.55,
              82.95,
              84.1,
              74.29,
              72.95,
              75.31,
              74.63,
              78.33,
              71.72,
              59.31,
              61.6,
              73.99,
              70.95,
              75.31,
              63.54,
              72.3,
              64.88,
              82.41,
              70.7,
              77.65,
              63.04,
              60.81])

linear_regression = LinearRegression()

x = x.reshape(-1, 1)

linear_regression.fit(x, y)

y_predicted = linear_regression.predict(x)

plt.scatter(x, y)
plt.plot(x, y_predicted, color="blue")
# plt.show()

print(linear_regression.coef_)
print(linear_regression.intercept_)

# y = 0.2733908x + 67.11163857012399

print("Hello")