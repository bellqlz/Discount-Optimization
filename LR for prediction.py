# LogisticRegression to obtain formulation about reactivation probability

from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

X_train=traina.drop('rebuy',axis=1)
Y_train=traina['rebuy']
X_test=predictnew01.drop('rebuy',axis=1).copy()



model = LogisticRegression()

model.fit(X_train,Y_train)

model.score(X_train,Y_train)

 

#Equation coefficient and Intercept

print('Coefficient:\n',model.coef_)

print('Intercept:\n',model.intercept_)

#Predict
predicted01=model.predict(X_test)
sum(predicted01)
acc_log = round(model.score(X_train, Y_train) * 100, 2)
print (acc_log)
#acc_log1 = round(model.score(X_test, Y_test) * 100, 2)
#print (acc_log1)

#predicted_a=pd.DataFrame(predicted01)
#predicted_a.to_csv($SAVE PATH$)
