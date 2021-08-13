from math import floor


akel_colors = {
    "Yellow1": (255, 255, 204),
    "Orange1": (253, 233, 217),
    "Blue1": (79, 129, 189),
    "Red1": (192, 80, 77),
    "Grey1": (217, 217, 217),
    "Grey2": (128, 128, 128),
    "Grey3": (191, 191, 191),
    "DarkGreen": (0, 176, 80),
    "Purple": (112, 48, 160),
    "Black": (0, 0, 0),
}


def cell_color(rng):
    """Returns cell color"""
    return rng.color


def akel_rgb(color):
    """Returns color as RGB"""
    return akel_colors[color]


def akel_single(color):
    """Returns color as single """
    return to_single(akel_rgb(color))


def to_single(color):
    """Returns RGB color as single color"""
    return (color[2] * 256 * 256) + (color[1] * 256) + (color[0])


def to_rgb(color):
    """Returns single color from RGB color"""
    return (
        floor(color % 256),
        floor((color / 256) % 256),
        floor((color / (256 * 256) % 256))
    )
