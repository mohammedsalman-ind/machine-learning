import pandas as pd 
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("logistic_regression_data.csv")
# print(df)
x = df[["Interview Score","Test Score"]]
y = df[["Selected"]]
model = LogisticRegression()
model.fit(x,y)
scored = int(input("Enter your interview score :"))
test_scored = int(input("Enter your Test score :"))
prid=model.predict([[scored , test_scored]])
