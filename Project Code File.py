import numpy as np
import pandas as pd

# Loaded the data
df_E=pd.read_excel('Hash-Analytic-Python-Analytics-Problem-case-study-Confirm.xlsx', sheet_name='Existing employees')
df_E.head()
df_L=pd.read_excel('Hash-Analytic-Python-Analytics-Problem-case-study-Confirm.xlsx', sheet_name='Employees who have left')
df_L.head()

# Combined the dataframes
df=pd.concat([df_E, df_L])
df.info()

# Defined the target variable and features
df_Target=df['Number of Employee']
df_Target.head()
df_feature=df.drop(['Number of Employee','dept','salary'], axis=1)
df_feature.tail()

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df_feature, df_Target, test_size=0.3, random_state=42)

#Using Logistic Regression(Algorithm provided a less effective result)
log=LogisticRegression()
log.fit(X_train,y_train)
y_pred=log.predict(X_test)
print(y_pred)

# Evaluated the model
from sklearn.metrics import accuracy_score
check= accuracy_score(y_test,y_pred)
print(check)
df_E=df.drop(['Number of Employee','dept','salary'], axis=1)
y_pd=log.predict(df_E)
print(y_pd)

#Using KNeihborsClassifier(Algorithm provided a better result)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(1)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
print(pred)

# Evaluated the model
from sklearn.metrics import accuracy_score
chk= accuracy_score(y_test,pred)
print(chk)

# Made predictions on the entire dataset
y_pd=knn.predict(df_E)
print(y_pd)

# Saved predictions to Excel
dR=df_E[['Emp ID']]
dR['Emp_Check']=y_pd
dR.to_excel('Prone_to_leave.xlsx',index=False)
