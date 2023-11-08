# Overfitting - where a model matches the training data almost perfectly,
# but does poorly in validation and other new data. 

# Underfitting - when a model fails to capture important distinctions
# and patterns in the data, so it performs poorly even in the training data.

# We care about accuracy on new data, which we estimate from our validation data.
# We want to find the sweet spot between underfitting and overfitting.

# In the image in this folder, we want to the low point on the (red) validtion curve.

# The max_leaf_nodes argument provides a very sensible way to control overfitting vs underfitting.
# The more leaves we allow (decision tree) the model to make, the more we move from the underfitting area
# to the overfitting area.
# A utility funciton can help compare MAE scores from different values for max_leaf_nodes.

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

# Data Loading Code Runs At This Point
import pandas as pd
    
# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)


# A for-loop can be used to compare the accuracy of models built with different values for max_leaf_nodes
# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae))

# Conclusion - Models can suffer from either
# Overfitting: capturing spurious patterns that won't recure in the future, leading to less accurate predictions
# Underfitting: failing to capture relevant patterns, leading to less accurate predictions.

# Use validation data, which isn't used in model training, to measure a candidate model's accuracy. 

print()