# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
print("SetUp Complete")

import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../path/file.csv'

# read the data and store data in DataFram titled '__ _ data'
melbourne_data = pd.read_csv(file_path)

# print a summary of the data in file path
melbourne_data.describe()

# see a list of all columns in the dataset
melbourne_data.columns

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# Use the dot notation to select the column we want to predict
# which is call the prediction target.
# By convention, the prediction target is called y.
# So the code needed to save the house prices in the data is
y = melbourne_data.Price

# The columns that are inputted into our model are called "features".
# For example, this would be columns used to determine the home price.
melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']

# By convention, this data is called X
X = melbourne_data[melbourne_features]

# Review the data using the describe() method and the head() method.
# Visually checking you data with these commands is an important part of 
# a data scientist's job. 
X.describe()

X.head()

# You will use the skikit-learn library to create models.
# When coding, the library is written as sklearn.
# Scikit-learn is a popular library for modeling the types of data 
# typically stored in DataFrames. 

# The steps to building and using a model are:
# 1. Define: What type of model will it be? A Decision Tree or some other model? 
# 2. Fit: Capture patterns from provided data. 
# 3. Predict: Just what is sounds like
# 4. Evaluate: Determine how accurate the model's predictions are. 

# Here's an example of defining a decision tree model with scikit-learn
# and fitting it with the features and target variable

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

# In practice, you'll want to make predictions for new houses coming on the market
# rather than the houses we already have prices for. But we'll make
# predictions for the first few rows of the training data to see how the predict fuction works.
predictions = melbourne_model.predict(X)
print(predictions)

print("First in-sample predictions:", melbourne_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

print(predictions)
print(melbourne_model.predict(X.head()))
y.head() # compare the top few predictions to the actual home values (in y).



