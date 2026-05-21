import numpy as np
import pandas as pd

#q: Load the dataset using Pandas.
print("**** Loading Dataset ****", end="\n")
df = pd.read_csv("student_scores.csv")


#q: Display the first 5 rows of the dataset.
print("-"*20)
print("**** First 5 rows ****", end="\n")
print(df.head())


#q: Check the data types of all columns.
print("-"*20)
print("**** Data type of all columns ****", end="\n")
print(df.dtypes)


#q: Find the total number of missing values in each column.
print("-"*20)
print("**** Total number of missing values in each column ****", end="\n")

print(df.isnull().sum())


#q: Create NumPy array from math_score column.
print("-"*20)
print("**** Create NumPy array from math_score column ****", end="\n")
#-->print(df["math_score"])--actual df column
math_scores = np.array(df["math_score"])
print(math_scores)


#q: Find the mean, median, maximum, and minimum values.
print("-"*20)
print("**** Find the mean, median, maximum, and minimum values ****", end="\n")

print("Mean:", np.mean(math_scores))
print("Median:", np.median(math_scores))
print("-"*20)
print("Minimum:", np.min(math_scores))
print("Maximum:", np.max(math_scores))


#q: Normalize the scores using NumPy.
print("-"*20)
print("**** Normalized scores of math column ****", end="\n")

normalized_scores = (math_scores - np.min(math_scores) / 
                     (np.max(math_scores) - (np.min(math_scores))))

print(normalized_scores)


#q: Identify and handle missing values.
print("-"*20)
print("**** Handling numerical And Categorical values ****", end="\n")

df["math_score"] = df["math_score"].fillna(df["math_score"].mean())
#-->print(df["math_score"])

df["science_score"] = df["science_score"].fillna(df["science_score"].mean())
#-->print(df["science_score"])

df["attendance"] = df["attendance"].fillna(df["attendance"].mean())
#-->print(df["attendance"])


#df["age"] = df["age"].fillna(df["age"].mode()[0])
#-->print(df["age"])

df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
#-->print(df["gender"])

df["exam_date"] = df["exam_date"].fillna(df["exam_date"].mode()[0])
#-->print(df["exam_date"])

print("--> Total missing values after updation :", end="\n")
print(df.isnull().sum())


#q: Find students with attendance below 70%.
print("-"*20)
print("**** Students with below 70% attendance are ****", end="\n")

print(df[ df["attendance"] < 70 ])


#q: Convert incorrect data formats into proper formats.
print("-"*20)
print("**** Convert incorrect data formats into proper formats ****", end="\n")

df["age"] = pd.to_numeric( df["age"] , errors= "coerce")
df["age"] = df["age"].fillna(df["age"].mean())
print(df["age"])

df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
print(df["gender"])

df["attendance"] = pd.to_numeric( df["attendance"] , errors = "coerce")
df["attendance"] = df["attendance"].fillna( df["attendance"].mean())
print(df["attendance"])

df["math_score"] = pd.to_numeric( df["math_score"] ,errors="coerce")
df["math_score"] = df["math_score"].fillna( df["math_score"].mean() )
print(df["math_score"])

df["science_score"] = pd.to_numeric( df["science_score"] ,errors="coerce")
df["science_score"] = df["science_score"].fillna( df["science_score"].mean() )
print(df["science_score"])


#q: Convert datetime
print("-"*20)
print("**** Convert datetime ****", end="\n")

df["exam_date"] = pd.to_datetime( df["exam_date"] ,errors= "coerce")
df["exam_date"] = df["exam_date"].fillna( df["exam_date"].mode()[0])
print(df["exam_date"])


#q: Detect and handle outliers in math_score and science_score columns.
print("-"*20)
print("**** Detect and handle outliers in math_score and science_score columns ****", end="\n")

Q1 = df["math_score"].quantile(0.25)
Q3 = df["math_score"].quantile(0.75)
Iqr = Q3 - Q1
lower_limit = Q1 - 1.5 * Iqr
upper_limit = Q3 - 1.5 * Iqr

print( df[ (df["math_score"] >= lower_limit) & (df["math_score"] <= upper_limit) ])

q1 = df["science_score"].quantile(0.25)
q3 = df["science_score"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 - 1.5 * iqr

print( df[ (df["science_score"] >= lower_limit) & (df["science_score"] <= upper_limit) ])


#q: Find and remove duplicate rows.
print("-"*20)
print("**** Finding and remove duplicate rows ****", end="\n")

print(df.duplicated().sum())
print(df.drop_duplicates())


#q: Create a new column named average_score.
print("-"*20)
print("**** Create a new column named average_score ****", end="\n")

df["average_score"] = ( df["math_score"] + df["science_score"] ) / 2
print(df["average_score"])


#q: Find top 5 students based on average_score.
print("-"*20)
print("**** Find top 5 students based on average_score ****", end="\n")

top_students = df.sort_values( by= "average_score" , ascending = False)
print(top_students.head(5))


#q: Calculate correlation between attendance and marks.
print("-"*20)
print("**** Calculate correlation between attendance and marks ****", end="\n")

correlation = df["attendance"].corr(df["average_score"])
print(correlation)


#q: Group students by gender and calculate average marks.
print("-"*20)
print("**** Group students by gender and calculate average marks ****", end="\n")

gender_average = df.groupby("gender")[["math_score", "science_score", "average_score"]].mean()
print(gender_average)