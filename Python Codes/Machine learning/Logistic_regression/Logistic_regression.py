#Keep all data and code in a same folder
import numpy as np
from numpy.lib.function_base import gradient 
import pandas as pd
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
class LogisticRegression:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #randomly assigning value of intercept
        self.intercept=np.zeros(x.shape[0])
        self.weight=np.zeros(x.shape[1])
        #z calculation
        self.z=np.dot(x, self.weight)+self.intercept
    def sigmoid(self,z):
       #calculate sigmoid
       return 1/(1+np.exp(-z))
    def loss(self,y_hat):
        
        return (-(self.y )* np.log(y_hat) - (1 - (self.y)) * np.log(1 - y_hat)).mean()
    def gradient_descent(self,y_hat):
        #calculates gradient descent for wieghts and intercept(dw,db)
        dw=np.dot(self.x.T, (y_hat - self.y)) / self.y.shape[0]
        db=np.sum((y_hat - self.y))/ self.y.shape[0]
        return dw,db
    def fit(self,lr,max_itr):
        x_point=[]
        y_point=[]
        #lr=learning rate
        #fitting the model
        for i in range(max_itr):
            y_hat=self.sigmoid(self.z)
            loss=self.loss(y_hat)
            
        
            x_point.append(i)
            y_point.append(loss)
            dw,db=self.gradient_descent(y_hat)
            #updating values of dw,db
            self.intercept-=lr*db
            self.weight-=lr*dw
            #updating values of Z
            self.z=np.dot(self.x, self.weight)+self.intercept
        return x_point,y_point #returns the x,y points for plotting
        
    def predict(self, x_test, treshold):
        #calculating the value of z
        z=np.dot(x_test, self.weight)+self.intercept[0]
        #calculating predicted value of y
        classification=self.sigmoid(z)
        for i in range(len(classification)):
            if classification[i]>=0.5:
                classification[i]=1
            else:
                 classification[i]=0
        return classification
    

def normalize(x):
    #features of data_set1 differ in ranges so normalising them to get a better fit
    m,n = x.shape
    # Normalizing all the n features of X.
    for i in range(n):
        x = (x- x.mean(axis=0))/x.std(axis=0)
    return x
def data_preparation(filename):
    data=pd.read_csv(filename)
    x1=np.array((list(data[data.columns[0]])))
    x2=np.array((list(data[data.columns[1]])))
    x=np.concatenate((x1.reshape(-1,1),x2.reshape(-1,1)),axis=1)
    y=np.array((list(data[data.columns[2]])))
    return x,y
def calculate_accuracy(y,y_pred):
    return sum(y_pred==y)/y.shape[0]

#training data preparation
x,y=data_preparation("ds1_train.csv")
#test data preparation
x_test,y_test=data_preparation("ds1_test.csv")

#Model
l_regressor=LogisticRegression(x,y)
x1_plot,y1_plot=l_regressor.fit(0.003,500)
y_pred_train=l_regressor.predict(x,0.5)
y_pred_test=l_regressor.predict(x_test,0.5)
#Accuracy part
print("Accuracy without normalisation:")
print(f"Accuracy for training set is {calculate_accuracy(y,y_pred_train)}")
print(f"Accuracy for testing set is {calculate_accuracy(y_test,y_pred_test)}")

#Normalising
x=normalize(x)
x_test=normalize(x_test)
l_regressor=LogisticRegression(x,y)
x2_plot,y2_plot=l_regressor.fit(0.4,560)
y_pred_train=l_regressor.predict(x,0.5)
y_pred_test=l_regressor.predict(x_test,0.5)
print("Accuracy without normalisation:")
print(f"Accuracy for training set is {calculate_accuracy(y,y_pred_train)}")
print(f"Accuracy for testing set is {calculate_accuracy(y_test,y_pred_test)}")

plt.subplot(1,2,1)
#plot without normalisation
plt.title("Without normalisation")
plt.xlabel('Iteration')
plt.ylabel('Losss')
plt.scatter(x1_plot,y1_plot)
plt.scatter(x1_plot[-1],y1_plot[-1],color="Red")
plt.subplot(1,2,2) 
#plot with normalisation
plt.title("With normalisation")
plt.xlabel('Iteration')
#plt.ylabel('Losss')
plt.scatter(x2_plot,y2_plot)  
plt.show()


        
        