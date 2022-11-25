import pandas as pd
import streamlit as st
import plotly.express as px

from database import view_all_customer
from database import view_all_admin
from database import view_all_data_dealer
from database import view_all_orders


# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID


def read(table):
    if table=='customer':
        result = view_all_customer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['cust_id','name','ph_no' ,'address','email_id' ,'password' ,'pan_no' ])
        with st.expander("View all customers"):
            st.dataframe(df)
        # with st.expander("user city"):
        #     task_df = df['city'].value_counts().to_frame()
        #     task_df = task_df.reset_index()
        #     st.dataframe(task_df)
        #     p1 = px.pie(task_df, names='index', values='city')
        #     st.plotly_chart(p1)


    elif table=='admin':
        result = view_all_admin()
        # st.write(result)
        df = pd.DataFrame(result, columns=['admin_id','admin_password'])
        with st.expander("View all admins"):
            st.dataframe(df)
        # with st.expander("user Bank_name"):
        #     task_df = df['bank_name'].value_counts().to_frame()
        #     task_df = task_df.reset_index()
        #     st.dataframe(task_df)
        #     p1 = px.pie(task_df, names='index', values='bank_name')
        #     st.plotly_chart(p1)

    elif table=='dealer':
        result = view_all_data_dealer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dealer_id','name','licence_no','location','admin'])
        with st.expander("View all dealers"):
            st.dataframe(df)
        # with st.expander("user promos"):
        #     task_df = df['usr_id'].value_counts().to_frame()
        #     task_df = task_df.reset_index()
        #     st.dataframe(task_df)
        #     p1 = px.pie(task_df, names='index', values='usr_id')
        #     st.plotly_chart(p1)


    elif table=='orders':
        result = view_all_orders()
        # st.write(result)
        df = pd.DataFrame(result, columns=['order_ID','order_date' ,'delivery_date' ,'cust_ID' ,'dealer_ID'])
        with st.expander("View all orders"):
            st.dataframe(df)
