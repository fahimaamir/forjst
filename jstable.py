import streamlit as st
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd


data = {
  "calories": [420, 380, 390],
  "mnammm": ['fffffff','gfdgdfgdf','gfhfghfgh' ],
  "duration": [50, 40, 45]
  
}

#load data into a DataFrame object:
df = pd.DataFrame(data)



t = pivot_ui(df)

with open(t.src) as t:
    components.html(t.read(), width=900, height=1000, scrolling=True)