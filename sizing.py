# import xlwings as xw
# wb = xw.books.active
# sht = wb.sheets.active
# rng = wb.selection


def display_height(rng):
    """Displays row height of each cell in selection."""
    for row in rng.rows:
        if row.api.EntireRow.Hidden == False:
            row.value = row.row_height


def set_height(rng):
    """Sets row height of each row in selection equal to value of selection."""
    for row in rng.rows:
        if row.api.EntireRow.Hidden == False:
            if row.value != None:
                row.row_height = row.value


def display_width(rng):
    """Displays row width of each cell in selection."""
    for column in rng.columns:
        if column.api.EntireRow.Hidden == False:
            column.value = column.column_width


def set_width(rng):
    """Sets column width of each column in selection equal to value of selection."""
    for column in rng.columns:
        if column.api.EntireRow.Hidden == False:
            if column.value != None:
                column.column_width = column.value
