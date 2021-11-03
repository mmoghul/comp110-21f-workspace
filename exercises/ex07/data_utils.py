"""Utility functions."""

__author__ = "123456789"

from csv import DictReader 

def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a csv into a 'table'. """
    result: list[dict[str, str]] = []
    
    # open a handle to the data file 
    file_handle = open (filename, "r", encoding="utf8") 

    # prepare to read data file as csv instead of simply as strings 
    csv_reader = DictReader(file_handle) 

    # read each row of the csv file line by line 
    for row in csv_reader:
        result.append(row) 

    # close file when done to free up resources
    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column. """ 
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result    


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Change a row-oriented table to colum-oriented table. """
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

def head(tabulate: dict[str, list[str]], N: [int]) -> dict[str, list[str]]: 
    """Produce a new column-based table with only the first `N` rows of data for each column. """
    result: dict[str, list[str]] = {}
    N: [int] = #first row of table 
    while N > 0: 
        store: list[str] = []
        N+=1 
        result.append(store)

    return result  

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]
    """Produce a new column-based table with two column-based tables combined. """
    result: dict[str, list[str]] = {}
     while table1 > 0: 
         N+=1 
        result.append(store)
    while table2 > 0: 

    #Loop through each of the columns _in the first parameter of the function_
    #1. Assign to the column key of the result dictionary the list of values stored in the first parameter at the same column
    #3. Loop through each of the columns _in the second parameter of the function_
    #1. If the current column key is already in the result dictionary, add on the list of values stored in the second parameter at the same column 
    #2. Otherwise, just assign to the column key of the result dictionary the list of values stored in the second parameter at the same column

def select(subset1: dict[str, list[str]], subset2: list[str]) -> dict[str, list[str]]:
   """Produce a new column-based table with only a specific subset of the original columns. """
   result: dict[str, list[str]] = {} 
   #Loop through each of the columns _in the second parameter of the function_
    #1. Assign to the column key of the result dictionary the list of values stored in the input dictionary at the same column 
