import streamlit as st
import pandas as pd
from database import loan


def loan_1():
    x = st.text_input("Enter dealer_id")
    if st.button('delete all orders'):
        df=pd.DataFrame(loan(int(x)),columns=['Validate'])
        st.dataframe(df)
