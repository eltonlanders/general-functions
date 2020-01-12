import numpy as np
import pandas as pd
titanic=pd.read_csv("C:/Users/elton/Downloads/titanic.csv")
#col=titanic.pivot_table(values=['Age','Survived'],index='Sex',aggfunc='mean')
#titanic_avg_age=titanic.merge(col,on=['Sex'],how='left')
#print(titanic_avg_age)
print(titanic['Fare'].nunique())