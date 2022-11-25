import streamlit as st
import pandas as pd
from database import aggregate_2
from database import aggregate
from database import aggregate_3
# from database import aggregate_4

def agg():

    if st.button('Display number of orders to be delivered on certain dates'):
        df=pd.DataFrame(aggregate(),columns=['delivery_date','Count'])
        st.dataframe(df)
    if st.button('Display number of dealers in the location'):
        df=pd.DataFrame(aggregate_2(),columns=['location','Total dealers'])
        st.dataframe(df)
    if st.button('Display number of dealers under the admins'):
        df=pd.DataFrame(aggregate_3(),columns=['admin','count'])
        st.dataframe(df)