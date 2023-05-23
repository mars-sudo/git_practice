# Code you have previously used to load data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalePrice
# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex5 import *
print("\nSetup complete")

# Validation model Mean Absolute Error
print(val_mae)

# Training model Mean Absolute Error
train_predictions = iowa_model.predict(train_X)
train_mae = mean_absolute_error(train_predictions, train_y)
print(train_mae)

# Function to test max_leaf_nodes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

# For loop that tries values for the max_leaf_nodes, then prints the possible values.
for max_leaf_nodes in [5, 25, 50, 100, 250, 500]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y )
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d"%(max_leaf_nodes, my_mae))

# This is to compare which leaf is the sweet spot MAE that is not overfitting or underfitting
print(val_mae)
print(train_mae)

# Store the best tree size as a variable.
best_tree_size = min(100, 250)

# You know the best tree size. If you were going to deploy this model in practice,
# you would make it even more accurate by using all the data and keeping that tree size.
# That is, you don't need to hold out the validation data now that you've made all your
# modeling decisions. 
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
final_model.fit(X, y)

# Decision Tree models are not very sophisticated by modern machine learning standards.
# Continue learning about Random Forests to improve models even more. 