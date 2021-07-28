import streamlit as st
import pandas as pd
from datetime import datetime
import xlwings as xw

wb = xw.books.active
sht = wb.sheets.active
rng = wb.selection


st.header("Excel Helper")
st.text("Add game below")

if st.button("Press me"):
    rng.value = 7
    st.write("You pressed me")