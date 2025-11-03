'''
Dataset ka total number of rows aur columns count karo.
Kitne employees “IT” department me kaam kar rahe hain?
Average salary nikal ke dikhao.
Highest salary wale employee ka naam aur department batao.
“Performance_Score” me kitne NaN values hain?
“Experience_Years” ke hisaab se salary ka average batao (group by).
Sirf “HR” department ke employees ka data dikhayo jinki salary 60,000 se zyada hai.
“Performance_Score” column me NaN values ko “Not Rated” se fill karo.
Dataset ko “Salary” ke descending order me sort karo.
30 saal se kam age wale kitne employees hai?
'''
import pandas as pd
df =pd.read_csv("employee_data.csv")
# answer one
# print(df.shape)

#answer two 
count_it_members= (df["Department"]=="IT").sum()
# print(count_it_members)

#answer three
avrg_salary =df["Salary"].mean()
# print(avrg_salary)

#answer four 
Hightest_salary = df["Salary"].max()
# print(Hightest_salary)

#answer five
highest = df.loc[df["Salary"].idxmax(),["Department","Salary","ID"]]
# location -> loc 
print(highest)
