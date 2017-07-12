import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./games.csv",header=0)
print(df.shape) #dimesnsions of csv matrix

# df=df.drop(['customerNo','firstName'],axis=1)
print(df.shape)
print(df.columns)
#print(df.head())
# print(df.tail(3))

#plt.hist(df["average_rating"])
#plt.show()
print(df.users_rated)
df=df[df["average_rating"]==0]
#print(df.tail(3))
#print(df.average_rating)
#print(df.users_rated)
print(df.tail(5))
df = df[df["users_rated"] > 0]
print(df.users_rated)
print(df.shape)
print(df.head(5))
df = df.dropna(axis=0)
print(df.head())
print(df.corr()["average_rating"])
