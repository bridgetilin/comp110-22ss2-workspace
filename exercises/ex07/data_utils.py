"""Dictionary related utility functions."""

__author__ = "730465834"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read that data file as CSV
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a non-empty row-oriented 'table' into a column-oriented one."""
    column_table: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]  # the first row of row_table will contain all of the column names
    for column in first_row:  
        column_table[column] = column_values(row_table, column) 

    return column_table


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with a specified number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    if len(column_table) <= rows:  # if the number of rows in the input table is less than the desired number of rows to be returned, return the entire input table
        return column_table
    for column in column_table:
        values: list[str] = []  
        counter: int = 0
        while counter < rows: 
            values.append(column_table[column][counter])
            counter += 1
        
        result[column] = values  

    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based 'table' with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]

    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table that is the combination of 2 other column-based tables."""
    result: dict[str, list[str]] = {}
    # loop through each of the columns in each of the 2 given tables
    for column_1 in column_table_1: 
        result[column_1] = column_table_1[column_1]
    for column_2 in column_table_2: 
        if column_2 in result:
            result[column_2] += column_table_2[column_2]  # if the current column key is already in result, add on the list of values stored at column_table_2 at the same column
        else:
            result[column_2] = column_table_2[column_2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list[str], produce a dict[str, int] whose key-value pairings consist of unique values in the given list and the number of times each value appeared."""
    result: dict[str, int] = {}
    for value in values:
        if value in result: 
            result[value] += 1 
        else:
            result[value] = 1
    return result 