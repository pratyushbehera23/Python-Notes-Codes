# Pandas

Pandas - open source 'data analysis' library in python
It leverages the power and speed of numpy to make data analysis and preprocessing easy for data scientists.

Why not MsExcel or such applications?
With MsExcel you cannot use python functions or ML implementations.
Plus with pandas data processing is precise, flexible, faster without limitations of excel sheets like size, loading..

Pandas has two types of data structures:

1. Series - 1D array with indexes, storing a single column or row of data in a dataframe. Simply a column or row in a DF.
2. Dataframe - tabular spreedsheet like representation with rows and columns.

> Jupyter notebook: open source web application to create documents that contain live code, equations, visualizations and narrative text.
It is mainly used for data analysis.
It supports programming languages: Python R Julia Scala ..

## Code

### Install

```sh
# need to have python installed

pip install pandas numpy jupyter
pip install --upgrade pandas

jupyter notebook
```

### Import and run

```py
import numpy as np
import pandas as pd
```

```py
dict1 = {
    "name":['XiaoYan', 'GuXuner', 'YaoLao'],
    "rank":[7, 8, 9],
    "level":['wang', 'huang', 'zuan']
}

df = pd.DataFrame(dict1)
# dataframe is simply representation in table excel like structure 
df # print/show

df.to_csv('btth.csv')
# this will export the data in a csv file (excel sheet)
df.to_csv('btth.csv', index=False) # without index

# Show Data
df.head(2) # top 2 rows
df.tail(2) # end 2 rows
df.shape # (rows, columns)
df.info() # info
df.describe() # statistical analysis of numericals

pokesheet = pd.read_csv('pokemons.csv') # read from file
pokesheet
pokesheet['Name'] # only name column
pokesheet['Name'][0] # of index 0
pokesheet.index = ['rank1', 'rank2', 'rank3', 'rank4'] # this will replace the regular index (row) ie. 01234..
pokesheet.index = list("ABCD") # this will replace the row index to ABCD.. ^same
pokesheet.columns = ['id', 'name', 'stat']  # this will change the column index/names
pokesheet.to_csv('pokemons.csv') # same name will put changes if done to data, or copy can be done with other name

```

```py
ser = pd.Series(np.random.rand(20))
ser # creates a series of random numbers from index 0 to 19
type(ser) # pandas.core.series.Series

newdf = pd.DataFrame(np.random.rand(100, 5), index=np.arange(100)) # 100 rows 5 columns of random numbers
newdf.head() # shows first 5 rows; remove .head() to show all 100 rows 
type(newdf) # pandas.core.frame.DataFrame

newdf.describe() # statistics
newdf.dtypes # data types of each columns
newdf.index # rows
newdf.columns # columns
newdf.to_numpy() # 
newdf.T # transpose
newdf.sort_index(axis=0, ascending=False) # axis=0(rows)/1(column) ascending=True(default)/False
newdf[0] # first column as Series
type(newdf[0]) # pandas.core.series.Series

newdf2 = newdf # X - it points to the same memory location ie. newdf == newdf2 always (both will show changes to one's).
newdf2 = newdf.copy() # O - copies the DF to this new variable as in separate lacation (or newdf[:])

newdf.loc[0,0] = 23 # puts 23 in position: row0-column0 
newdf.column = list("ABCDE")
newdf.loc[0,'A'] = 23 # puts 23 in position: row0-columnA 

newdf.drop([0]) # remove row-0
newdf.drop('E', axis=1) # remove column E (temporary/toShow)
newdf = newdf.drop('E', axis=1) # remove column E (permanent)
newdf.drop(['A', 'C'], axis=1) # remove column A,C (temporary)
newdf.drop(['A', 'C'], axis=1, inplace=True) # remove column A,C (permanent)

newdf.loc[[1,2], ['C','D']] # shows rows-1,2 and column-C,D as table ie. 4 elements/cells
newdf.loc[:, ['C','D']] # shows all rows and column-C,D as table
newdf.loc[[1,2], :] # shows rows-1,2 and all columns as table
newdf.loc[(newdf['A']<0.3)] # shows all rows where data in row-A < 0.3
newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)] # shows all rows where data in row-A < 0.3 and in row-C > 0.1

newdf.iloc[0,2] # shows the data in row-0 col-2
newdf.iloc[[0,1], [1,2]] # row-0,1 col-B,C

newdf.reset_index()
newdf.reset_index(drop=True)
newdf.reset_index(drop=True, inplace=True)
newdf.head(3)

newdf['B'].isnull() # check the column for null value and show True
newdf.loc[:, ['B']] = None # all None
newdf['B'].isnull() # all True now
newdf.loc[:, ['B']] = 10 # all 10

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

```py
df.mean()
df.corr()
df.count()
df.max()
df.min()
df.median()
df.std()
```

```sh
pip install xlrd # needed for using excel in pandas (else the below code will throw error)
```

```py
# Excel
data = pd.read_excel('data.xlsx')
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')
data
```

```py
Tweets = pd.DataFrame([], columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

```
