import streamlit as st
import eda
import prediction
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["EDA", 'Prediction'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

if selected == 'EDA':
    eda.run()
else:
    prediction.run()