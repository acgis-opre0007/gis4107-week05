def create_cell_refs(columns,rows):
    """
    Given arguments of strings of column and row IDs, creates a comma-separated list of all cell references
    in the resulting table.
    columns -- space-delimited column identifiers as capital letters starting from A
    rows -- index number starting from 1
    """
    
    result = ''
    column_idList = columns.split()
    row_idList = rows.split()

    for x in range(len(column_idList)):
        for y in range(len(row_idList)):
            result += f',{column_idList[x]}{row_idList[y]}'
    result = result[1:len(result)]
    return result