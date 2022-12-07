import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('Pune house data Updated Dataset.csv')
print(df)

print(df.columns)

df['No of Bedrooms ']=df['No of Bedrooms '].fillna(0)

print(df)

model_input_slice = df.iloc[:,:-1]
model_input_slice

model_prediction_slice = df.iloc[:,-1:]
#model_prediction_slice

train_x,test_x,train_y,test_y = train_test_split(model_input_slice,model_prediction_slice,test_size=0.10,random_state=5)

regression_model = LinearRegression()

regression_model.fit(train_x,train_y)

# predicted_price = regression_model.predict(test_x)
# #predicted_price

# input_values = [[3,2,1132.0,2,1,96]]
# predicted_price1 = regression_model.predict(input_values)
# print(predicted_price1)


pickle.dump(regression_model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))