def table_highligher(rng):
    """Highlights each other row in selection if the row is not hidden in light blue"""
    from itertools import cycle
    mycolor = cycle([None, (231, 238, 245)])

    for row in rng.rows:
        if row.api.EntireRow.Hidden == False:
            row.color = next(mycolor)


def table_grey_lines(rng):
    """Makes grey top and bottom lines for each line in table"""
    import borders
    # Excludes first and last row
    for row in [r for r in rng.rows][1:-1]:
        if row.api.EntireRow.Hidden == False:
            borders.borderer(row, thickness='thin',
                             placement='top', color='Grey3')
            borders.borderer(row, thickness='thin',
                             placement='bottom', color='Grey3')
