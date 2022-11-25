import streamlit as st
import pandas as pd
from database import joining_2
from database import joining
from database import joining_3


def join():

    if st.button('Finding name of the dealer for a particular order'):
        df=pd.DataFrame(joining(),columns=['order_id','dealer_name'])
        st.dataframe(df)
    if st.button('Finding address for a order'):
        df=pd.DataFrame(joining_2(),columns=['order_id','address'])
        st.dataframe(df)

    if st.button('hackjoin'):
        df=pd.DataFrame(joining_3(),columns=['dealer_id','dealer_name','admin','admin_password'])
        st.dataframe(df)
    