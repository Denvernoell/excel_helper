import streamlit as st
import pyperclip
import xlwings as xw
from pathlib import Path

# app = xw.App(visible=False, add_book=False)


app = xw.apps.active
wb = app.books.active
sht = wb.sheets.active
rng = wb.selection
ps = sht.api.PageSetup

file_path = Path(wb.fullname)
folder_path = file_path.parent
workbook_name = file_path.name


my_action = st.sidebar.radio(
    'Action', ['PDF', 'Sizing', 'Page Setup', 'Tables'])


st.title('Akel Helper')
st.subheader(my_action)
st.markdown(f"""
Workbook: {workbook_name}

Sheet: {sht.name}
""")
# -------------------------- Addresses -------------------------------------
if my_action == 'Address':
    row_absolute = st.checkbox('row absolute')
    column_absolute = st.checkbox('column absolute')
    include_sheetname = st.checkbox('include sheetname')
    external = st.checkbox('external')
    if st.button('Show address'):
        # st.write(address_type)

        my_address = rng.get_address(
            row_absolute=row_absolute,
            column_absolute=column_absolute,
            include_sheetname=include_sheetname,
            external=external
        )
        pyperclip.copy(my_address)
        st.write(str(my_address))
        # st.markdown(my_address)

# -------------------------- Pdfing -------------------------------------

if my_action == 'PDF':
    import pdfing

    c1, c2 = st.beta_columns(2)

    with c1:
        pdf_types = ['current', 'chapter', 'all']
        for t in pdf_types:
            if st.button(t):
                app.screen_updating = False
                pdfing.export_pdf(wb, quantity=t)
                app.screen_updating = True
                st.success(pyperclip.paste())
    with c2:
        # with st.beta_expander("Help"):
        st.video('pdfing.webm')

if my_action == 'Page Setup':

    # Print settings
    import print_settings

    page_type = st.radio('Page Type', ['Table', 'Figure'])

    orienation = st.radio('Orienation', ['Portrait', 'Landscape'])
    size = st.radio('Page Size', ['Normal', 'Extended'])
    width = st.number_input('Width', min_value=1)
    height = st.number_input('Height', min_value=1)
    if st.button('Set Page Size'):
        print_settings.margins(ps, page_type)
        print_settings.print_properties(ps, orienation, size, width, height)


# -------------------------- Colors -------------------------------------

if my_action == 'colors':
    if st.button('Display color'):
        import colors
        st.write(colors.cell_color(rng))

# -------------------------- Sizing -------------------------------------

if my_action == 'Sizing':
    import sizing

    a, b = st.beta_columns(2)

    sizing_dict = {
        'Display Height': sizing.display_height,
        'Set Height': sizing.set_height,
        'Display Width': sizing.display_width,
        'Set Width': sizing.set_width,
    }
    # image_dict = {
    #     'Display Height': '.\\right-arrow-forward.png',
    #     'Set Height': '.\\right-arrow-forward.png',
    #     'Display Width': '.\\right-arrow-forward.png',
    #     'Set Width': '.\\right-arrow-forward.png',
    # }
    # st.image('.\\right-arrow-forward.png')
    c1, c2 = st.beta_columns(2)

    with c1:
        for key, value in sizing_dict.items():
            # st.beta_columns(len(sizing_dict))
            if st.button(key):
                value(rng)
    with c2:
        st.video('Sizing.webm')

# -------------------------- Tables -------------------------------------
if my_action == 'Tables':
    import tables
    import borders

    options_dict = {
        'Highlighter': tables.table_highligher,
        'Grey borders': tables.table_grey_lines,
    }

    c1, c2 = st.beta_columns(2)

    with c1:
        for key, value in options_dict.items():
            # st.beta_columns(len(sizing_dict))
            if st.button(key):
                value(rng)
    with c2:
        st.video('Tables.webm')
