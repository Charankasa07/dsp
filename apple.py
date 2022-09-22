
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def check(a,b,c,x):  
    if (b>=a and c<=a):
        df=pd.read_csv('apple.csv')
        day_u=df['Day'].unique()
        day_l=[]
        for i in day_u:
            day_l+=[i.lower()]
        if (x.lower() in day_l):
            openi=[]
            highi=[]
            lowi=[]
            closei=[]
            for j in range(len(df.index)):
                if (x.lower()==df.loc[j].Day.lower()):
                    openi+=[df.loc[j].Open]
                    highi+=[df.loc[j].High]
                    lowi+=[df.loc[j].Low]
                    closei+=[df.loc[j].Close]
            data=pd.DataFrame({"Open":openi,"High":highi,"Low":lowi,"Close":closei})
            new_data=pd.DataFrame({"Open":a,"High":b,"Low":c},index=[0])
            pred(data,new_data)    
        elif (x.lower()=='saturday' or x.lower()=='sunday'):
            st.success("{} is Holiday".format(x.title()))
        else:
            st.success("Give valid day")
    else:
        st.success("Please Give Valid Data!!! \n Make sure that High Price must be equal or greater than Open Price and Low price must be equal or less than Open Price")
def pred(data,new_data):
    x=data[['Open','High','Low']]
    y=data['Close']
    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
    regressor=LinearRegression()
    regressor.fit(x_train,y_train)
    pred=regressor.predict(new_data)
    st.success('Predicted Closing Price:{}'.format(pred[0]))
def main():
    st.title("Stock Closing Price Prediction - APPLE")

    open_price=st.number_input("Open Price")
    high_price=st.number_input("High Price")
    low_price=st.number_input("Low Price")
    day=st.text_input("Day")
  
    if st.button("Predict"):
        check(open_price,high_price,low_price,day)
main()
