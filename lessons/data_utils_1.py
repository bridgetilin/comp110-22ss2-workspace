"""Some helpful utility functions for working with CSV files."""


from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    # returns a list of dict[str, str] each row is represented as a dictionary (key = column name, value = values associated)
    # creates a row-oriented table
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str,str]] = []
    
    # Open a handle to the data file, built in python notation 
    # "r" indicates "read"
    file_handle = open(filename, "r", encoding="utf8")

    # prepare to read that data file as CSV row-by-row rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # close file when done to free its resources.
    file_handle.close()

    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transformm a row-oriented table to a column oritented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]  # the first row contains all of the column names
    for column in first_row:
        result[column] = column_values(row_table, column)  # column_values gives you all of the values in a single column

    return result

