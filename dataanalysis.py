import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

#Display the first few rows of the data
print(df.head())

#Describe the data, get descriptive statistics for all numerical column
print(df.describe())

#Find the missing values in each column
mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

#Find the average value Form the any table
avg = df['Age'].mean()
print(f"Average of age: {avg}")


#Count the unique values from the any table
uv = df['Age'].nunique()
print(f"unique values: {uv}")

#Filter rows based on a condition from any table
eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

#Find the maximum salary from any table
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary'] == max_salary]
print("Highest paid employee: \n", max_salary_emp)

#Count frequency of each value in a column from a table
dep_count = df['Department'].value_counts()
print("Number of emplouee in each deperment: \n", dep_count)

#Sort data by a column from a table
sort = df.sort_values(by='Age', ascending=False)
print("Senior to Junior employee: \n", sort)

#Experience the Emoplyee declear from any colume
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>=30 else 'Junior')
print("Data with Experinece column:\n", df)

#data visualization
 
#plot a pie chat
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()