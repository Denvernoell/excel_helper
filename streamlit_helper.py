import streamlit as st
import pyperclip
import xlwings as xw
from pathlib import Path

# app = xw.App(visible=False, add_book=False)
app = xw.apps.active
# wb = xw.books.active
wb = app.books.active
sht = wb.sheets.active
rng = wb.selection


file_path = Path(wb.fullname)
folder_path = file_path.parent

# All
# my_action = st.sidebar.radio(
#     'Action', ['address', 'borders', 'colors', 'pdf', 'sizing'])

# Partial
my_action = st.sidebar.radio(
    'Action', ['pdf', 'sizing'])


st.title('Akel Helper')
st.subheader(my_action)
# -------------------------- Addresses -------------------------------------
if my_action == 'address':
    # address_type = st.multiselect('address type', [
    #                               'row absolute', 'column absolute', 'include sheetname', 'external'])

    # # st.write(address_type)
    # if st.button('Show address'):
    #     # st.write(address_type)
    #     row_absolute = 'row absolute' in address_type
    #     column_absolute = 'column absolute' in address_type
    #     include_sheetname = 'include sheetname' in address_type
    #     external = 'external' in address_type

    #     my_address = rng.get_address(row_absolute=row_absolute, column_absolute=column_absolute,
    #                                  include_sheetname=include_sheetname, external=external)
    #     pyperclip.copy(my_address)
    #     st.write(my_address)

    # address_type = st.multiselect('address type', [
    #                               'row absolute', 'column absolute', 'include sheetname', 'external'])

    # st.write(address_type)
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

if my_action == 'pdf':
    import pdfing

    pdf_types = ['current', 'chapter', 'all']
    for t in pdf_types:
        if st.button(t):
            app.screen_updating = False
            pdfing.export_pdf(wb, quantity=t)
            app.screen_updating = True


# -------------------------- Borders -------------------------------------

if my_action == 'borders':
    if st.button('Create border'):
        import borders
        borders.borderer(rng)
# -------------------------- Colors -------------------------------------

if my_action == 'colors':
    if st.button('Display color'):
        import colors
        st.write(colors.cell_color(rng))

# -------------------------- Sizing -------------------------------------

if my_action == 'sizing':
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
    for key, value in sizing_dict.items():
        # st.beta_columns(len(sizing_dict))
        if st.button(key):
            value(rng)
