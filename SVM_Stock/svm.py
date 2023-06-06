
#Description: This program predicts the price of FB stock for a specific day
#             using the Machine Learning algorithm called 
#             Support Vector Regression (SVR) Model

#import the packages
import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

#Load the data
#from google.colab import files # Use to load data on Google Colab
#uploaded = files.upload() # Use to load data on Google Colab
df = pd.read_csv('FB_30_days.csv')
df.head(7)

#Get the number of rows and columns in the data set
df.shape

#Print the last row of data (this will be the that we test on)
df.tail(1)

#Get all of the data except for the last row
df = df.head(len(df)-1)
print(df.shape)

df_dates = df.loc[:,'Date'] # Get all of the rows from the Date column
df_open = df.loc[:,'Open'] #Get all of the rows from the Open column

dates = [[int(date.split('-')[2])] for date in df_dates]
prices = [float(open_price) for open_price in df_open]
#See what days were recoreded in teh data set
print(dates)

#Function to make predictions using 3 different support vector regression models with 3 different kernals
def predict_prices(dates, prices, x):
  
  #Create 3 Support Vector Regression Models
  svr_lin = SVR(kernel='linear', C=1e3)
  svr_poly = SVR(kernel='poly', C=1e3, degree=2)
  svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
  
  #Train the models on the dates and prices
  svr_lin.fit(dates,prices)
  svr_poly.fit(dates, prices)
  svr_rbf.fit(dates, prices)
  
  #Plot the models on a graph to see which has the best fit
  plt.scatter(dates, prices, color = 'black', label='Data')
  plt.plot(dates, svr_rbf.predict(dates), color = 'red', label='RBF model')
  plt.plot(dates, svr_lin.predict(dates), color = 'green', label='Linear model')
  plt.plot(dates, svr_poly.predict(dates), color = 'blue', label='Polynomial model')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.title('Support Vector Regression')
  plt.legend()
  plt.show()
  
  #return all three model predictions
  return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

#Predict the price of FB on day 31
predicted_price = predict_prices(dates, prices, [[31]])
print(predicted_price)
