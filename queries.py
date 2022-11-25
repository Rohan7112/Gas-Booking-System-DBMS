import streamlit as st
import pandas as pd
from database import query_1


def execute_query():
        col1, col2 = st.columns(2)
        l=[]
        with col1:
            c1 = st.text_input("c1:")
            c2 = st.text_input("c2:")
            c3 =  st.text_input("c3:")
            c4 =  st.text_input("c4:")
            c5 =  st.text_input("c5:")

        with col2:
            c6 = st.text_input("c6:")
            c7 = st.text_input("c7:")
            c8 = st.text_input("c8:")
            c9 = st.text_input("c9:")
            c10 = st.text_input("c10:")
        query = st.text_input("query:")

        if c1!='':
            l.append(c1)
        if c2!='':
            l.append(c2)
        if c3!='':
            l.append(c3)
        if c4!='':
            l.append(c4)
        if c5!='':
            l.append(c5)
        if c6!='':
            l.append(c6)
        if c7!='':
            l.append(c7)
        if c8!='':
            l.append(c8)
        if c9!='':
            l.append(c9)
        if c10!='':
            l.append(c10)

        if st.button('calc'):
            df = pd.DataFrame(query_1(query), columns=l)
            st.dataframe(df)