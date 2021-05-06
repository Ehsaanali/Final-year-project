
# Create your views here.
from django.shortcuts import render;
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn import metrics
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy import stats
def Forecasting(request):
    return render(request,'Forecasting.html')
 

def result(request):
    
    data = pd.read_csv("data/2017_2018_2019_2020.csv")
   
    le = LabelEncoder()

    dfle = data
    le.fit_transform(dfle.District)
    dfle.District = le.fit_transform(dfle.District)
    
    pdata = np.abs(stats.zscore(data))
    df = data[(pdata<3).all(axis=1)]
    
    x = data.drop('Total Pop Covered', axis=1)
   
    y =data['Total Pop Covered']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.30)
    model = LinearRegression()
    model.fit(x_train, y_train)

    var = str(request.GET['m'])
    var1= int(request.GET['m1'])
    var2= int(request.GET['m2'])
    #m1 =[var,var1,var2,178938,848,810901,1908804,43234]
    #m2 =[var,var1,var2,1788,848,810901,19804,543]
    #m3 =[var,var1,var2,1938,48,901,804,64353]
    #m4 =[var,var1,var2,1788,848,810901,19804,6546]
    #m5 =[var,var1,var2,1938,48,1,4,7546]
    #m6 =[var,var1,var2,178938,848,810901,1908804,6454]
    #m7 =[var,var1,var2,1788,848,810901,19804,424]
    #m8 =[var,var1,var2,1938,48,901,804,765]
    #m9 =[var,var1,var2,1788,848,810901,19804,7565]
    #m10 =[var,var1,var2,1938,48,1,4,857]
    #m11 =[var,var1,var2,178938,848,810901,1908804,5234]
    #m12 =[var,var1,var2,1788,848,810901,19804,2444443]


    #m= [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12] 
    lst = []

    pred = model.predict(np.array([var, var1, var2, 434344 , 23232, 999 ,23, 2121]).reshape(1, -1))
    pred2 = model.predict(np.array([var, var1, var2, 444 , 23232, 232 , 2323, 2121]).reshape(1, -1))
    pred3 = model.predict(np.array([var, var1, var2, 111344 , 9999, 23232 , 233, 2121]).reshape(1, -1))
    pred4 = model.predict(np.array([var, var1, var2, 434344 , 23232, 999 ,23, 2121]).reshape(1, -1))
    pred5 = model.predict(np.array([var, var1, var2, 444 , 23232, 232 , 2323, 2121]).reshape(1, -1))
    pred6 = model.predict(np.array([var, var1, var2, 111344 , 9999, 23232 , 233, 2121]).reshape(1, -1))
    
    p =[pred, pred2, pred3,pred4,pred5,pred6]
    pred = round(pred[0])
    lst.append(p)
    arr = np.array(lst)
    num = arr.tolist() 
        
        
    return render(request, 'Forecasting.html',{"result2": num})