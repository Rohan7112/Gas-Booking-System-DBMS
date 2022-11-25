import pandas as pd
import streamlit as st

from database import view_all_customer
from database import view_all_admin
from database import view_all_data_dealer
from database import view_all_orders


from database import view_only_customer
from database import view_only_admin
from database import view_only_dealer
from database import view_only_orders

from database import delete_customer
from database import delete_admin
from database import delete_dealer
from database import delete_order

# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID


def delete(table):
    if table=='customer':
        result = view_all_customer()
        df = pd.DataFrame(result, columns=['cust_id','name','ph_no' ,'address' ,'email_id' ,'password' ,'pan_no'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_customer()]
        selected_user = st.selectbox("customer to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete user"):
            delete_customer(selected_user)
            st.success("customer has been deleted successfully")
        new_result = view_all_customer()
        df2 = pd.DataFrame(new_result, columns=['cust_id','name','ph_no' ,'address' ,'email_id' ,'password' ,'pan_no'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='admin':
        result = view_all_admin()
        df = pd.DataFrame(result, columns=['admin_id','admin_password'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_admin = [i[0] for i in view_only_admin()]
        selected_admin = st.selectbox("admin to Delete", list_of_admin)
        st.warning("Do you want to delete ::{}".format(selected_admin))
        if st.button("Delete admin"):
            delete_admin(selected_admin)
            st.success("Admin has been deleted successfully")
        new_result = view_all_admin()
        df2 = pd.DataFrame(new_result, columns=['admin_id','admin_password'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='dealer':
        result = view_all_data_dealer()
        df = pd.DataFrame(result, columns=['dealer_id','name','licence_no','location','admin'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealer = [i[0] for i in view_only_dealer()]
        selected_dealer = st.selectbox("Dealer to Delete", list_of_dealer)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete dealer"):
            delete_dealer(selected_dealer)
            st.success("dealer has been deleted successfully")
        new_result = view_all_data_dealer()
        df2 = pd.DataFrame(new_result, columns=['dealer_id','name','licence_no','location','admin'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='orders':
        result = view_all_orders()
        df = pd.DataFrame(result, columns=['order_ID','order_date' ,'delivery_date' ,'cust_ID' ,'dealer_ID'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_order = [i[0] for i in view_only_orders()]
        selected_order = st.selectbox("order to Delete", list_of_order)
        st.warning("Do you want to delete ::{}".format(selected_order))
        if st.button("Delete order"):
            delete_order(selected_order)
            st.success("Order has been deleted successfully")
        new_result = view_all_data_dealer()
        df2 = pd.DataFrame(new_result, columns=['order_ID','order_date' ,'delivery_date' ,'cust_ID' ,'dealer_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
