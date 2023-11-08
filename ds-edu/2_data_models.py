# Model Validation
# Evaluate every model that is built.
# In most applications, the relevant measure of model quality is predictive accuracy.
# Will the model's predictions be close to what actually happens?

# One metric for summarizing model quality is Mean Absolute Error (MAE)
# The prediction error for each house is
# error = actual - predicted

# So if the house cost $150,000 and you predict $100,000, the error is $50,000

# With MAE, we take the absoulte value of each error; this converts each error to 
# a positive number. We then take the average of those absolute errors.
# This is a measure of model quality. 
# "On average, our predictions are off by about X"

# To calculate MAE, we first need a model. 

# ~ code snip ~
from sklearn.tree import DecisionTreeRegressor

# Define model. 
melbourne_model = DecisionTreeRegressor()

# Fit model
melbourne_model.fit(X, y)

# Once we have a model, we calculate the mean absoulte error
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# The above measure is an "in-sample" score, we used a single "sample" of houses
# for both building the model and evaluating it - this is bad. 

# Since model's practical value come from making predictions on new data, 
# we measure performance on data that wasn't used to build the model.
# The most straightforward way to do this is to exclude some data from 
# the model-building process, and then use those to test the model's 
# accuracy on data it hasn't seen before. This data is called validation data.

# The skikit-learn library has a function train_test_split
# this breaks up data into two pieces. We'll use some fo that data as training data
# to fit the model. We'll use the other data as validation data to calculate MAE.

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target.
# The split is based on a random number generator. Supplying a numeric value 
# to the random_state argument gaurantees we get the same split every time we run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Define model
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit training model
melbourne_model.fit(train_X, train_y)

# Get the predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

# Print the top few validation predictions
print(melbourne_model.predict(val_X.head()))
# Print the top few actul prices from validation data
print(melbourne_model.predict(train_X.head()))

