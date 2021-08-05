from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import os
import pyperclip
import xlwings as xw
wb = xw.books.active


def create_room(file_path):
    """Takes file path and moves it to OldPdfs in order to create room to make another file with the same name"""

    p = Path(file_path)
    try:
        os.makedirs(Path(f"{p.parent}/OldPdfs"))
    except:
        pass

    num_list = ["1st", "2nd", "3rd"] + [f"{i}th" for i in range(4, 100)]
    for i in num_list:
        try:
            replacement_path = (Path(f"{p.parent}\OldPdfs\{i}{p.name}"))
            os.rename(p, replacement_path)
            break
        except:
            continue


# create_room("P:\Support\Admin\Timesheets\Denver Noell_MISC\work_scripts\Akel_helper\Replacent_alternatives_071921.pdf")


def reorder_pdf(file_path, order_list):
    """Takes file path and order list and reorders the pages in the file to match the order_list"""

    pdf_writer = PdfFileWriter()

    source = PdfFileReader(str(replacement_path))
    for new_page in order_list:

        for page in range(source.getNumPages()):
            page += 1
            if page == new_page:
                pdf_writer.addPage(source.getPage(page - 1))
                break

    with open(p, 'wb') as out:
        pdf_writer.write(out)


# reorder_pdf(".pdf", [3, 6, 9, 1, 4, 7, 2, 5, 8])


def export_pdf(wb, quantity='current'):
    """Creates PDF of all dark green sheets in workbook"""
    from datetime import datetime
    import colors
    sht = wb.sheets.active
    from pathlib import Path
    import subprocess
    import re

    file_path = Path(wb.fullname)
    folder_path = file_path.parent
    wb_name_with_date = file_path.stem
    wb_name = re.sub(r'_\d{6}', '', wb_name_with_date)

    todays_date = datetime.strftime(datetime.now(), '%m%d%y')

    if quantity == 'current':
        pdf_name = f"{sht.name}_{todays_date}.pdf"
        my_sheets = sht.name

    if quantity == 'chapter':
        # [colors.to_rgb(s.api.Tab.Color) for s in wb.sheets]

        chapter_starts = {
            s.name: s.index for s in wb.sheets if s.api.Tab.Color == colors.akel_single("Purple")}
        chapter_starts['end'] = wb.sheets[-1].index

        green_sheets = {
            s.name: s.index for s in wb.sheets if s.api.Tab.Color == colors.akel_single("DarkGreen")}

        chapter, sht_start = [
            [key, value] for key, value in chapter_starts.items() if value < sht.index][-1]
        sht_end = [value for key, value in chapter_starts.items()
                   if value > sht_start][0]
        my_sheets = [key for key, value in green_sheets.items()
                     if sht_start <= value <= sht_end]
        pdf_name = f"{wb_name}_{chapter.strip()}_{todays_date}.pdf"

    if quantity == 'all':
        pdf_name = f"{wb_name}_{todays_date}.pdf"
        my_sheets = [s.name for s in wb.sheets if s.api.Tab.Color ==
                     colors.akel_single("DarkGreen")]

    pdf_path = str(folder_path / pdf_name)
    create_room(pdf_path)
    wb.to_pdf(pdf_path, include=my_sheets)
    os.system(pdf_path)
    subprocess.Popen([pdf_path], shell=True)
    pyperclip.copy(pdf_path)

    # quantities = {
    #     'current':
    # }
# export_pdf(wb, quantity='current')
