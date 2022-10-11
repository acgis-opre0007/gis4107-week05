import excel_utils

def test_excel_utils(columns,rows):
    return excel_utils.create_cell_refs(columns,rows)

print(f'\nExpected: A1,A2,B1,B2\nActual: {test_excel_utils("A B","1 2")}')