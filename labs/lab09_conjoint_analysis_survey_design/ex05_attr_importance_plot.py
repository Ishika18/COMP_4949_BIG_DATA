import matplotlib.pyplot as plt

carAttributes = ['Safety', 'Fuel Economy', 'Accessories']
importanceLevels = [61.5384615, 7.69230769, 30.7692308]
plt.bar(carAttributes, importanceLevels)
plt.xticks(rotation=75)
plt.title("Car Attribute Importance")
plt.show()
