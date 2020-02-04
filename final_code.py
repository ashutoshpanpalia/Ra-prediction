import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

df = pd.read_csv(r"C:\Users\Ashutosh\Desktop\Project\Project Regression\Final Code\algo.csv")
print(df.shape) # To check the dimension of dataset
print(df.head()) # To print first 10 data points
X=df.iloc[:,0:4]
y=df.iloc[:,4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)
y_test_predict = pol_reg.predict(poly_reg.fit_transform(X_test)) # predicting on test data-set
# evaluating the model on test dataset
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_predict))
r2_test = r2_score(y_test, y_test_predict)
mae= mean_absolute_error(y_test, y_test_predict)
mape= mean_absolute_percentage_error(y_test, y_test_predict)
print("R2 score of testing set is {}".format(r2_test))
print("RMSE of testing set is {}".format(rmse_test))
print("MAE of testing set is {}".format(mae))
print("MAPE of testing set is {}".format(mape))

#PlOTTING OF PREDICTED Ra
c =  50000
num = range(0,600)
x_graph = np.zeros(600)
y_graph = np.zeros(600)
for i in num:
    x_graph[i]=i #x_graph[i]=c for peripheral length vs Ra
    print(pol_reg.predict(poly_reg.fit_transform([[c,32,0.05,.3]])))
    y_graph[i] = pol_reg.predict(poly_reg.fit_transform([[c,32,0.05,.3]]))
    i=i+1
    c=c+10000
plt.plot(x_graph , y_graph)
# naming the x axis
plt.xlabel('No. of workpieces')
# naming the y axis
plt.ylabel('Ra predicted')
# giving a title to my graph
plt.title('Increase of surface roughness as the tool gets worn out')
# function to show the plot
plt.show()
print('END')
