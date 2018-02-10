# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc=cars.loc[:,"cars_per_cap"]
many_cars=cpc>500
car_maniac=cars[many_cars]


# Print car_maniac
print(car_maniac)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium=cars[np.logical_and(cars['cars_per_cap']>100,cars['cars_per_cap']<500)]
# Print medium
print(medium)
