import streamlit as st
import pandas as pd
from database import info


def info_1():
    if st.button('Display the information by using Procedure'):
        df=pd.DataFrame(info(),columns=['First_name','Last_name','Email'])
        st.dataframe(df)