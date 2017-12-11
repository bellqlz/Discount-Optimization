# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 03:08:29 2017
　
@author: jdbel
　
Aim: predict the reactivation in predict set.
"""
　
import pandas as pd

　
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
len(discount.promotionid_received.unique())
v1=discount.loc[discount['promotionid_received']==194886,:]
v2=discount.loc[discount['promotionid_received']==194882,:]
v3=discount.loc[discount['promotionid_received']==194898,:]
v4=discount.loc[discount['promotionid_received']==194891,:]
　
　
# deal with data
　
newtrain=pd.merge(training,discount,how='left',on='promotionid_received')
newtrain01=pd.merge(newtrain,user,how='left',on='userid')
newtrain01.info()
newtrain01.head()
print(newtrain01.columns.values)
del newtrain01['birthday']
del newtrain01['email_verified']
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
del newtrain02['max_value_x']
del newtrain02['gender']
newtrain02=newtrain02.fillna(0)
newtrain02.describe()
　
newtrain03=newtrain02
newtrain03['active']=newtrain03['active_0']+newtrain03['active_1']+newtrain03['active_2']+newtrain03['active_3']+newtrain03['active_4']+newtrain03['active_5']+newtrain03['active_6']+newtrain03['active_7']+newtrain03['active_8']+newtrain03['active_9']+newtrain03['active_20']+newtrain03['active_21']+newtrain03['active_22']+newtrain03['active_23']+newtrain03['active_24']+newtrain03['active_25']+newtrain03['active_26']+newtrain03['active_27']+newtrain03['active_28']+newtrain03['active_29']+newtrain03['active_30']+newtrain03['active_10']+newtrain03['active_11']+newtrain03['active_12']+newtrain03['active_13']+newtrain03['active_14']+newtrain03['active_15']+newtrain03['active_16']+newtrain03['active_17']+newtrain03['active_18']+newtrain03['active_19']
newtrain03=newtrain03.drop(newtrain03.columns[9:39],axis=1)
newtrain03=newtrain03.drop('active_0',axis=1)
newtrain03=newtrain03.drop('discount_y',axis=1)
newtrain03.rename(columns={'discount_x':'discount'},inplace=True)
newtrain03.active[newtrain03.active.astype(int)<10]=1
newtrain03.active[newtrain03.active.astype(int)>=10]=2
newtrain03.discount_x[newtrain03.discount==20]=1
newtrain03.discount_x[newtrain03.discount==30]=2
newtrain03.discount_x[newtrain03.discount==50]=3
print(len(newtrain03.userid.unique()))
　
newpredict01=pd.merge(predict,discount,how='left',on='promotionid_received')
newpredict01=newpredict01[['userid','discount']]
use=newtrain03[['userid','is_seller','active']]
newpredict01=pd.merge(newpredict01,use,how='left',on='userid')
newpredict01=newpredict01.drop_duplicates()
print(len(newpredict01.userid.unique()))
newpredict01=newpredict01.fillna(0)
dp=newpredict01[newpredict01.duplicated(['userid','discount'])==True]
dp01=newpredict01[newpredict01.duplicated(['userid','discount'])==False]
dp01.discount[newpredict01.discount==20]=1
dp01.discount[newpredict01.discount==30]=2
dp01.discount[newpredict01.discount==50]=3
　
newtrain03=newtrain03.drop('userid',axis=1)
dp01=dp01.drop('userid',axis=1)
　
#divide into 5 groups for different target: used, repurchase_15...
train15=newtrain03[['repurchase_15?','discount','is_seller','active']]
train30=newtrain03[['repurchase_30?','discount','is_seller','active']]
train60=newtrain03[['repurchase_60?','discount','is_seller','active']]
train90=newtrain03[['repurchase_90?','discount','is_seller','active']]
train_u=newtrain03[['used?','discount','is_seller','active']]
