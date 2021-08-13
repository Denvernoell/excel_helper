# import pyperclip
# import xlwings as xw
# from pathlib import Path


# app = xw.apps.active
# wb = app.books.active
# sht = wb.sheets.active
# rng = wb.selection
# ps = sht.api.PageSetup


# PrintType = "Table"
# PrintType = "Figure"


def InchesToPoints(inches):
    return inches * 72.0


def margins(ps, PrintType):

    if PrintType == "Table":
        ps.LeftMargin = InchesToPoints(0.5)
        ps.RightMargin = InchesToPoints(0.5)
        ps.TopMargin = InchesToPoints(0.5)
        ps.BottomMargin = InchesToPoints(0.5)
        ps.HeaderMargin = InchesToPoints(0)
        ps.FooterMargin = InchesToPoints(0)
        ps.CenterHorizontally = True
        ps.CenterVertically = False

    if PrintType == "Figure":
        ps.LeftMargin = InchesToPoints(0)
        ps.RightMargin = InchesToPoints(0)
        ps.TopMargin = InchesToPoints(0)
        ps.BottomMargin = InchesToPoints(0)
        ps.HeaderMargin = InchesToPoints(0)
        ps.FooterMargin = InchesToPoints(0)
        ps.CenterHorizontally = True
        ps.CenterVertically = False


def print_properties(ps, orienation, size, width, height):
    orientations = {
        "Portrait": 1,
        "Landscape": 2,
    }
    sizes = {
        "Normal": 1,
        "Extended": 3,
    }

    # Orientation
    # 1 = Portrait
    # 2 = Landscape

    # PaperSize
    # 8.5 x 11 = 1
    # 11 x 17 = 3

    ps.Orientation = orientations[orienation]
    ps.PaperSize = sizes[size]
    ps.FitToPagesWide = width
    ps.FitToPagesTall = height

    #     print(ps.Orientation)
    #     print(ps.PaperSize)
    #     print(ps.FitToPagesWide)
    #     print(ps.FitToPagesTall)
