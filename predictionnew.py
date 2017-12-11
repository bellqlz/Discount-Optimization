# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 03:56:54 2017
　
@author: jdbel
　
Aim: divide customers into groups based on their features via unsupervised algorithm--LR
"""
　
import pandas as pd
# import data

　
#observe and analyze data one by one
　
training.head()
len(training['userid','promotionid_received'].unique())
print(training.columns.values)
training.info()
len(training.userid.unique())
training.describe(include=['O'])
　
transaction.head()
　
log0.head()
　
data.head()
len(data.userid.unique())
　
predict.head()
predict.info()
predict.voucher_code_received.unique()
predict.promotionid_received.unique()
len(predict.promotionid_received.unique())
print(predict.columns.values)
　
len(user.userid.unique())
print(user.head())
print(user.tail())
user.info()
　
discount.head()
discount.discount.unique()
len(discount.promotionid_received.unique())# know the voucher type
v1=discount.loc[discount['promotionid_received']==194886,:]#confrim the discount in predict data
v2=discount.loc[discount['promotionid_received']==194882,:]
v3=discount.loc[discount['promotionid_received']==194898,:]
v4=discount.loc[discount['promotionid_received']==194891,:]
　
　
# deal with data
　
newtrain=pd.merge(training,discount,how='left',on='promotionid_received')
newtrain01=pd.merge(newtrain,user,how='left',on='userid')
newtrain01.info()
newtrain01.head()
print(newtrain01.columns.values)
del newtrain01['birthday']# delete column that has too much missing value
del newtrain01['email_verified']#delete irrelevant or unspecified data
del newtrain01['phone_verified']
del newtrain01['registration_time']
del newtrain01['voucher_received_time']
del newtrain01['voucher_code_received']
　
len(active.voucher_received_date.unique())
active.head()
del active['voucher_code_received']
del active['voucher_received_time']
del active['voucher_received_date']
　
dis=pd.merge(active,discount,how='left',on='promotionid_received')
newtrain02=pd.merge(newtrain01,dis,how='left',on=['userid','promotionid_received'])
del newtrain02['promotionid_received']
del newtrain02['max_value_y']
newtrain02.tail()
newtrain02.info()
newtrain02.describe(include=['O'])
len(newtrain02.userid.unique())
　
print(newtrain02.columns.values)
del newtrain02['max_value_x']#delete duplicate item
del newtrain02['gender']#'gender' miss much values
newtrain02=newtrain02.fillna(0)
newtrain02.describe()
　
newtrain03=newtrain02# the days repurchase can be seen as '1'
newtrain03['reactive']=newtrain03['repurchase_90?']+newtrain03['repurchase_60?']+newtrain03['repurchase_30?']+newtrain03['repurchase_15?']
newtrain03.reactive[newtrain03.reactive.astype(int)>0]=1
newtrain03=newtrain03.drop(newtrain03.columns[3:5],axis=1)
newtrain03=newtrain03.drop('repurchase_15?',1)
newtrain03=newtrain03.drop('repurchase_90?',1)
　
newtrain03.info()#active should be classified to simplify
newtrain03['active']=newtrain03['active_0']+newtrain03['active_1']+newtrain03['active_2']+newtrain03['active_3']+newtrain03['active_4']+newtrain03['active_5']+newtrain03['active_6']+newtrain03['active_7']+newtrain03['active_8']+newtrain03['active_9']+newtrain03['active_20']+newtrain03['active_21']+newtrain03['active_22']+newtrain03['active_23']+newtrain03['active_24']+newtrain03['active_25']+newtrain03['active_26']+newtrain03['active_27']+newtrain03['active_28']+newtrain03['active_29']+newtrain03['active_30']+newtrain03['active_10']+newtrain03['active_11']+newtrain03['active_12']+newtrain03['active_13']+newtrain03['active_14']+newtrain03['active_15']+newtrain03['active_16']+newtrain03['active_17']+newtrain03['active_18']+newtrain03['active_19']
newtrain03=newtrain03.drop(newtrain03.columns[5:35],axis=1)
del newtrain03['active_0']
del newtrain03['discount_y']
newtrain03['active'].describe()
　
newtrain03.active[newtrain03.active.astype(int)<10]=1
newtrain03.active[newtrain03.active.astype(int)>=10]=2
newtrain03['active'].describe()
　
newtrain03['rebuy']=newtrain03['used?']+newtrain03['reactive']#used and repurchase both can be seen as reactivate so that combine them
newtrain03.rebuy[newtrain03.rebuy>0]=1
del newtrain03['used?']
del newtrain03['reactive']
　
newtrain03.discount_x[newtrain03.discount_x==20]=1#discount value should be normalization 
newtrain03.discount_x[newtrain03.discount_x==30]=2
newtrain03.discount_x[newtrain03.discount_x==50]=3
　
#divide into two groups based on customers active session
print(len(newtrain03.active.unique()))
newtrain03.describe()
traina=newtrain03.loc[newtrain03['active']==1,:]
trainb=newtrain03.loc[newtrain03['active']==2,:]
　
newpredict=pd.merge(predict,discount,how='left',on='promotionid_received')
newpredict=newpredict[['userid','discount']]
use=newtrain03[['userid','is_seller','active','rebuy']]
newpredict=pd.merge(newpredict,use,how='left',on='userid')
newpredict=newpredict.drop_duplicates()
print(len(newpredict.userid.unique()))
print(newpredict.active.unique())
newpredict=newpredict.fillna(0)
dp=newpredict[newpredict.duplicated(['userid','discount'])==False]
dp.discount[newpredict.discount==20]=1
dp.discount[newpredict.discount==30]=2
dp.discount[newpredict.discount==50]=3
dp.describe()
print(len(dp.active.unique()))
　
predictnew01=dp.loc[dp['active']<=1,:]
predictnew02=dp.loc[dp['active']==2,:]
　
　
traina.rename(columns={'discount_x':'discount'},inplace=True)
trainb.rename(columns={'discount_x':'discount'},inplace=True)
　
predictnew01=predictnew01.drop(['userid','active'],axis=1)
predictnew02=predictnew02.drop(['userid','active'],axis=1)
traina=traina.drop(['userid','active'],axis=1)
trainb=trainb.drop(['userid','active'],axis=1)
　
len(predictnew01['used?'][predictnew01['used?']==1])
len(predictnew02['reactive'][predictnew02['reactive']==1])
　
