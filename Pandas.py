#One way to build a DataFrame is from a dictionary.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd
# Create dictionary my_dict with three key:value pairs:
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap':cpc}
# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)
# Print cars
print(cars)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index=row_labels
# Print cars again
print(cars)

#___________CSV to DataFrame (1)________-
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv')

# Print out cars
print(cars)

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)
# Print out cars
print(cars)


###______pandas_access to data
#____square brackets
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars [['country', 'drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#________loc , iloc

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc["JAP"])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', "EG"]])
print(cars.iloc[[1,6]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])


# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
