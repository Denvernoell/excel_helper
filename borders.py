def borderer(rng, thickness='thick', placement='all', color='Black'):
    """Adds border to selection"""
    if thickness == 'thin':
        weight = 2

    if thickness == 'thick':
        weight = 3

    # 7 through 13 == xlEdgeTop,xlEdgeBottom,xlEdgeRight,xlEdgeLeft,xlInsideHorizontal,xlInsideVertical
    borders = {
        'all': '',
        'top': 3,
        'bottom': 4,
        'right': 2,
        'left': 1,
    }
    if placement == 'all':
        for i in range(7, 11):
            # rng.api.Borders(i).Weight=weight
            # sht.range(rng.address).api.Borders(i).Weight = weight
            border = rng.api.Borders(i)
    else:
        # sht.range(rng.address).api.Borders(borders[placement]).Weight = weight
        border = rng.api.Borders(borders[placement])

    border.Weight = weight

    import colors
    border.Color = colors.akel_single(color)
