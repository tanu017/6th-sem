import numpy as np 
from sklearn.linear_model import LinearRegression

x = np.array([[1000, 2], [1500, 3], [1200, 2], [1800, 4], [900, 2], [2000, 3]])
y = np.array([300000, 450000, 350000, 500000, 280000, 450000])
model = LinearRegression()
model.fit(x, y)
size = float(input("Enter the size of the house in square feet: "))
bedrooms = int(input("Enter the number of bedrooms: "))
new_data = np.array([[size, bedrooms]])
predicted_price = model.predict(new_data)
print("Predicted price for a house with size {} sqft and {} bedrooms: Rs. {:.2f}".format(size, bedrooms, predicted_price[0]))