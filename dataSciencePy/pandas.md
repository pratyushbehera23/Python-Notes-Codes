# Pandas

Pandas is an open source __data analysis__ library in python used for _analysing, cleaning and exploring data_.

It leverages the power and speed of numpy to make data analysis and preprocessing easy for data scientists.

Why use pandas inplace of MsExcel or such applications?

- Using _Pandas_ you can implement python functions and ML algos to you dataset.
- Also, _Pandas_ data processing is precise, flexible, faster without limitations like of excelsheets like size, loading time, etc.

## Code

### Installation

What we need for data science and stuff?

- Python
- Pandas, other libs like numpy, matplotlib, ..
- Jupyter

```sh
# Need to have Python installed

# Here we install important packages like numpy, jupyter along with pandas
pip install pandas numpy jupyter
# If you have installed pandas earlier, you can update it
pip install --upgrade pandas

# Using pandas in jupyter notebook is always advantageous
jupyter notebook
```

> Jupyter notebook is an open source web application to create documents that contain live code, equations, visualizations and narrative text.
Mainly used for data analysis and supports programming languages: Python R Julia Scala ..

### Import and run

```py
# Import numpy and pandas
import numpy as np
import pandas as pd
```

Pandas has two types of data structures:

1. Series - 1D array with indexes, storing a single column or row of data in a dataframe. Simply a column or row in a DF.
2. Dataframe - tabular spreedsheet like representation with rows and columns.

#### Create

##### from CSV

```py
df = pd.read_csv('myfile.csv')
```

##### from Dicitionary

```py
tempdc = {'c1':[1,2,3], 'c2':[4,5,6], 'c3':[7,8,9]}
df = pd.DataFrame.from_dict(tempdc)

# Data
myCharacters = {
    "name":['XiaoYan', 'GuXuner', 'YaoLao'],
    "rank":[7, 8, 9],
    "level":['wang', 'huang', 'zuan']
}
df = pd.DataFrame(myCharacters)

```

#### Read

```py
df # print/show top and bottom 5 rows
df.head(10) # top 10 rows
df.tail(10) # end 10 rows
df.index # all rows
df.columns # all columns names
df.dtypes # all columns datatypes
df.shape # size (rows, columns)
df.info() # info
df.describe() # statistical summary of data(int/floats)
df.describe(include='object') # statistical summary of data(objects)
```

#### Filter

```py
df.colname # prints specific column (or key)
df['col name'] # if column name (or key) is multiword
df[['colname', 'col name']] # show multiple columns
df.colname.unique() # prints uniques values
df[df['colname']=='value'] # prints only rows that satisfies the condition
df[(df['colname']=='5') & (df['colname2']==False)] # ^
```

#### Index

```py
df.column = list("ABCDE") # changes column names to A, B, C,..
```

##### with iloc

```py
# iloc uses index
df.iloc[0] # row at index 0
df.ilic[0:15] # rows 0 to 15 indexed
df.iloc[0, 0] # first value in row at index 0
df.iloc[0, -1] # last value in row at index 0
df.iloc[0,2] # shows the data in row-0 col-2
df.iloc[[0,1], [1,2]] # row-0,1 col-1,2 (col-B,C)
```

##### with loc

```py
# loc uses index or keywords(colnames)
df.loc[0,0] = 23 # puts 23 in position: row0-column0 
df.loc[0,'A'] = 23 # puts 23 in position: row0-columnA 
df.loc[[1,2], ['C','D']] # shows rows-1,2 and column-C,D as table ie. 4 elements/cells
df.loc[:, ['C','D']] # shows all rows and column-C,D as table
df.loc[[1,2], :] # shows rows-1,2 and all columns as table
df.loc[(df['A']<0.3)] # shows all rows where data in row-A < 0.3
df.loc[(df['A']<0.3) & (df['C']>0.1)] # shows all rows where data in row-A < 0.3 and in row-C > 0.1
```

#### Update

```py
# df.isnull().sum()
df.dropna() # drop all rows with NA (to show only)
df.dropna(inplace=True) # drop all rows with NA (from the df)
df.dropna(how='all', axis=1) # drop column where all elements is NA
df.drop_duplicates(subset=['name']) # drop row where there is duplicate name (more than 1 except the first)
df.drop_duplicates(subset=['name'], keep='last') # drop row where there is duplicate name (more than 1 except the last)
df.drop_duplicates(subset=['name'], keep=False) # drop row where there is duplicate name (all)
df['name'].value_counts(dropna=False) # counts how many same values
df.isnull() # show null places as True
df.notnull() # show not null places as True
```

#### Methods

```py
df['colname'].mean()
df['colname'].corr()
df['colname'].count()
df['colname'].max()
df['colname'].min()
df['colname'].median()
df['colname'].std()
df['colname'].value_counts()
```

#### Exporting data

```py
df.to_csv('btth.csv') # this will export the data in a csv file (excel sheet)
df.to_csv('btth.csv', index=False) # without index
```

#### Importing and using data from a csv file

```py
pokesheet = pd.read_csv('pokemons.csv') # read from file
pokesheet # shows data
pokesheet['Name'] # only name column
pokesheet['Name'][0] # of index 0
pokesheet.index = ['rank1', 'rank2', 'rank3', 'rank4'] # this will replace the regular index (row) ie. 01234..
pokesheet.index = list("ABCD") # this will replace the row index to ABCD.. ^same
pokesheet.columns = ['id', 'name', 'stat']  # this will change the column index/names
pokesheet.to_csv('pokemons.csv') # same name will put changes if done to data, or copy can be done with other name
```

#### Importing Excel file

```sh
# This is needed for using excel file in pandas (else the code will throw error)
pip install xlrd
```

```py
data = pd.read_excel('data.xlsx')
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')
data # shows data
```

#### Taking random numbers as elements

```py
ser = pd.Series(np.random.rand(20)) # creates a series of random numbers from index 0 to 19
type(ser) # pandas.core.series.Series
ser # shows data

newdf = pd.DataFrame(np.random.rand(100, 5), index=np.arange(100)) # 100 rows 5 columns of random numbers
type(newdf) # pandas.core.frame.DataFrame
newdf.head() # shows first 5 rows; remove .head() to show all 100 rows 
```

```py
newdf.to_numpy() # 
newdf.T # transpose
df.sort_index(axis=0, ascending=False) # axis=0(rows)/1(column) ascending=True(default)/False
newdf[0] # first column as Series
type(newdf[0]) # pandas.core.series.Series

newdf2 = newdf # X - it points to the same memory location ie. newdf == newdf2 always (both will show changes to one's).
newdf2 = newdf.copy() # O - copies the DF to this new variable as in separate lacation (or newdf[:])

newdf.drop([0]) # remove row-0
newdf.drop('E', axis=1) # remove column E (temporary/toShow)
newdf = newdf.drop('E', axis=1) # remove column E (permanent)
newdf.drop(['A', 'C'], axis=1) # remove column A,C (temporary)
newdf.drop(['A', 'C'], axis=1, inplace=True) # remove column A,C (permanent)

newdf.reset_index()
newdf.reset_index(drop=True)
newdf.reset_index(drop=True, inplace=True)
newdf.head(3)

newdf['B'].isnull() # check the column for null value and show True
newdf.loc[:, ['B']] = None # all None
newdf['B'].isnull() # all True now
newdf.loc[:, ['B']] = 10 # all 10
```

```py
df = pd.DataFrame({"rank":[1, np.nan, 3], "name":['Charmender', 'Bulbasaur', 'Squirtle'], "born":[pd.NaT, pd.NaT, pd.Timestamp("1990-02-23")]})
df.head()
df.dropna() # drop all rows with NA
df.dropna(how='all', axis=1) # drop column where all elements is NA
df.drop_duplicates(subset=['name']) # drop row where there is duplicate name (more than 1 except the first)
df.drop_duplicates(subset=['name'], keep='last') # drop row where there is duplicate name (more than 1 except the last)
df.drop_duplicates(subset=['name'], keep=False) # drop row where there is duplicate name (all)
df['name'].value_counts(dropna=False) # counts how many same values
df.isnull() # show null places as True
df.notnull() # show not null places as True
```

## Leetcode Pandas QnAs

```py
Tweets = pd.DataFrame([], columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

```
