import pandas as pd
import numpy as np

s = pd.Series([1,2,3,np.nan,6,8])

dates = pd.date_range("20130101",periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))

df2= pd.DataFrame({"A": 1.,
                   "B":pd.Timestamp("20130102"),
                   "C": pd.Series(1, index=list(range(4)),dtype="float32"),
                   "D": np.array([3]*4,dtype="int32"),
                   "E": pd.Categorical(["test","train","test","train"]),
                   "F":"foo"})
#print(df2.dtypes)

#VIEW DATA
#print(df.head())
#print(df.tail(3))
#print(df.index)
#print(df.columns)
df.sort_values(by="B")

#use it for comparing
print(df)

#GETTING
#print(df["A"])
#print(df[0:3])
#print(df["20130102":"20130104"])

#SELECTION BY LABEL
#print(df.loc[dates[0]])
#print(df.loc[:,["A","B"]])
#print(df.loc["20130102":"20130104",["A","B"]])

#SELECTION BY POSITION
#print(df.iloc[3])
#print(df.iloc[3:5,0:2])
#print(df.iloc[[1,2,4],[0,2]])
#print(df.iloc[1:3,:])
#print(df.iloc[:,1:3])