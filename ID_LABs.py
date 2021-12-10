# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:00:23 2021

@author: $udo
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotyly.graph_objects as go
from warnings import filterwarnings
filterwarnings ('ignore')
df = pd.read_xls("cost.xls")
#change the columns
df.colums = ['City', 'Salary', 'Groceries','Housing', 'Utilities','Transportation', 'Healthcare']
fig = px.scatter(dfmer[~dfmer.City.isna()], x="City(%)", y="Salary", animation_frame="Groceries", size="Housing", color="Utilities", hover_name"City", log_x=True, size_max=60, range_x=[4,100], range_y[1000,4500], text="City"
fig.show
City_cor = {}
for i in dfmer.City.unique():
    cor_val = dfmer[fmer.City == i] [['Salary','Groceries' ]].corr().iloc[0,1]City_corr[i]=corr_val
max(City_corr, key=City_corr. get), City_corr[max(City_corr, key=Citycorr.get)] ('New York', 136024)
coefficient = cal_coefficient(X_train, y_train)
intercept - cal_intercept(X_train, y_test)
df_City['y1'] = predict(df+City['Salary'],coefficient,intercept)
from skleran.linear_model import LinearRegression
from sklearn.metrics import r2_score
lr_  linearRegression()
lr.fit(X_train, y_train)
sk_predicted_y = lr.predict(X_test)
y_all = lr.predict(df_City['Salary'].values.reshape(-1,1))
df_City['y'] =y_all
sk_r2 _ r2_score(df_City['Cost%'], df_City ['y'])
print(f 'SK R square:{sk_r2}')