def borderer(rng, thickness='thick', placement='all'):
    """Adds border to selection"""
    if thickness == 'thin':
        weight = 2

    if thickness == 'thick':
        weight = 3

    # 7 through 13 == xlEdgeTop,xlEdgeBottom,xlEdgeRight,xlEdgeLeft,xlInsideHorizontal,xlInsideVertical
    borders = {
        'all': '',
        'top': 7,
        'bottom': 8,
        'right': 9,
        'left': 10,
    }
    if placement == 'all':
        for i in range(7, 11):
            # rng.api.Borders(i).Weight=weight
            # sht.range(rng.address).api.Borders(i).Weight = weight
            rng.api.Borders(i).Weight = weight
    else:
        # sht.range(rng.address).api.Borders(borders[placement]).Weight = weight
        rng.api.Borders(borders[placement]).Weight = weight
