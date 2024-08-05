# pandas is a data analysis library that allows us to easily read and work with different types of data
# We can use this library to analyse csv, Excel files
# It has a great performance since it is built on top of NumPy

import pandas as pd

base_dir = "/Users/dharanikumar/PycharmProjects/PythonLearningProject/Data"
df = pd.read_csv(f"{base_dir}/stackoverflow_data/survey_results_public.csv")  # read_csv will help us to read the data from a csv file
# dataframes are pretty much the backbone for pandas
# dataframes are basically rows and columns of data

print(df)
print(df.shape)  # shape attribute gives us the number of rows and columns in a tuple form
print(df.info())  # the info method gives the number of rows and columns along with the datatype of all the columns

pd.set_option("display.max_columns", 85)  # this setting helps us to view the max of 85 columns in the output
pd.set_option("display.max_rows", 85)  # this setting helps us to view the max of 85 rows in the output
schema_df = pd.read_csv(f"{base_dir}/stackoverflow_data/survey_results_schema.csv")
print(schema_df.head())  # will show only the top 5 rows
print(schema_df.head(10))  # will show only the top 10 rows
print(schema_df.tail())  # will show only the last 5 rows
print(schema_df.tail(10))  # will show only the last 10 rows

people = {
    "first": ["Dharani", "Shiv", "John"],
    "last": ["Kumar", "Raj", "Doe"],
    "email": ["gopavaram.dharani@gmail.com", "shiv@apple.com", "john-doe@apple.com"]
}

data_df = pd.DataFrame(people)  # creating a dataframe from dict which has multiple values for a key
print(data_df)
print(data_df['email'])  # accessing a specific column in a dataframe
print(data_df.email)  # we can also use dot notation to access data of a particular column
# prefer using the square bracket notation because when we use dot notation we might the column might look as an attribute for the dataframe

print(type(data_df['email']))  # <class 'pandas.core.series.Series'>
# A series is just a list of data but with a dataframe it has lot more functionality
# A series is basically a rows of a single column
# A dataframe is basically a container for multiple series objects

print(data_df[['last', 'email']])  # way to access multiple columns from the dataframe
print(type(data_df[['last', 'email']]))  # the type is not a series anymore because we are retrieving multiple columns
# Instead it is another dataframe
print(data_df.columns)  # To know the column names in the dataframe

print(data_df.iloc[0])  # To view the first row
print(data_df.iloc[2])
print(data_df.iloc[[1, 2]])  # To view the specific rows
print(data_df.iloc[[1, 2], [1, 2]])  # To view the specific row and column

print(data_df.loc[0])  # To view the first row using loc function
print(data_df.loc[[0, 1]])  # To view the first and second row
print(data_df.loc[[0, 1], ["email", "last"]])

# Let's use these methods we learnt on a large dataframe

print(df.columns)
print(schema_df.columns)
print(df["CodingActivities"])
print(df["CodingActivities"].value_counts())  # returns the count of every type of value present inside the column
print(df.loc[1, "CodingActivities"])  # To view the data of CodingActivities column for the first row
print(df.loc[[1, 2, 3], "CodingActivities"])
print(df.loc[0:5, "CodingActivities"])  # We can use slicing instead of specifying the rows in list
# Here the last index of the slice is inclusive unlike slice operator
print(df.loc[0:5, "CodingActivities": "YearsCodePro"])  # We can slice columns as well

print(data_df.set_index('email'))  # setting the email as the index for dataframe
print(data_df)
# all the dataframe operations doesn't modify the original dataframe instead it creates a new one
# If you want to edit the dataframe in place then we need to use the below command
data_df.set_index('email', inplace=True)
print(data_df)
print(data_df.index)  # To know the index of a dataframe
print(schema_df.index)  # If we don't set an index for a dataframe then by default it is RangeIndex(start=0, stop=78, step=1)


