import datetime

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


from database import get_cust_id
from database import get_admin_id
from database import get_dealer_id
from database import get_order_id


from database import edit_customer_data
from database import edit_admin_data
from database import edit_dealer_data
from database import edit_orders_data

# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID



def update(table):
    if table=='customer':
        result = view_all_customer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['cust_id','name','ph_no' ,'address' ,'email_id' ,'password' ,'pan_no'])
        with st.expander("Current customers"):
            st.dataframe(df)
        list_of_customers = [i[0] for i in view_only_customer()]
        selected_customer = st.selectbox("customer to Edit", list_of_customers)
        selected_result = get_cust_id(selected_customer)
        # st.write(selected_result)
        if selected_result:
            cust_id = selected_result[0][0]
            name = selected_result[0][1]
            ph_no = selected_result[0][2]
            address = selected_result[0][3]
            email_id = selected_result[0][4]
            password = selected_result[0][5]
            pan_no = selected_result[0][6]
            
            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_cust_id = st.text_input("cust_id:",cust_id)
                new_name = st.text_input("name:", name)
                new_ph_no = st.text_input("ph_no:", ph_no)
                new_address = st.text_input("address:", address)
            with col2:
                new_email_id = st.text_input("email_id:",email_id)
                new_password = st.text_input("password:",password)
                new_pan_no = st.text_input("pan_no:",pan_no)
                
            if st.button("Update user_account"):
                edit_customer_data(new_cust_id,new_name,new_ph_no ,new_address ,new_email_id ,new_password ,new_pan_no,cust_id,name,ph_no ,address ,email_id ,password ,pan_no)
                st.success("Successfully updated:: {} to ::{}".format(cust_id, new_cust_id))

        result2 = view_all_customer()
        df2 = pd.DataFrame(result2, columns=['cust_id','name','ph_no' ,'address' ,'email_id' ,'password' ,'pan_no'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='admin':
        result = view_all_admin()
        # st.write(result)
        df = pd.DataFrame(result, columns=['admin_id','admin_password'])
        with st.expander("Current admins"):
            st.dataframe(df)
        list_of_admins = [i[0] for i in view_only_admin()]
        selected_admin = st.selectbox("admin to Edit", list_of_admins)
        selected_result = get_admin_id(selected_admin)
        # st.write(selected_result)
        if selected_result:
            admin_id = selected_result[0][0]
            admin_password = selected_result[0][1]
            

            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_admin_id = st.text_input("admin_id:",admin_id)
                
            with col2:
                new_admin_password = st.text_input("admin_password:", admin_password)
                
            if st.button("Update admin"):
                edit_admin_data(new_admin_id,new_admin_password,admin_id, admin_password)
                st.success("Successfully updated:: {} to ::{}".format(admin_id, new_admin_id))

        result2 = view_all_admin()
        df2 = pd.DataFrame(result2, columns=['admin_id','admin_password'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='dealer':
        result = view_all_data_dealer()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dealer_id','name','licence_no','location','admin'])
        with st.expander("Current dealer"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_dealer()]
        selected_dealer = st.selectbox("dealer to Edit", list_of_dealers)
        selected_result = get_dealer_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            dealer_id = selected_result[0][0]
            name = selected_result[0][1]
            licence_no = selected_result[0][2]
            location = selected_result[0][3]
            admin = selected_result[0][4]
            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_dealer_id = st.text_input("dealer_id:",dealer_id)
                new_name = st.text_input("name:", name)
                new_licence_no = st.text_input("licence_no:", licence_no)
                
            with col2:
                new_location = st.text_input("location:",location)
                new_admin = st.text_input("admin:",admin)

            if st.button("Update dealer"):
                edit_dealer_data(new_dealer_id,new_name,new_licence_no,new_location,new_admin,dealer_id,name,licence_no,location,admin)
                st.success("Successfully updated:: {} to ::{}".format(dealer_id, new_dealer_id))

        result2 = view_all_data_dealer()
        df2 = pd.DataFrame(result2, columns=['dealer_id','name','licence_no','location','admin'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='orders':
        result = view_all_orders()
        # st.write(result)
        df = pd.DataFrame(result, columns=['order_ID','order_date' ,'delivery_date' ,'cust_ID' ,'dealer_ID'])
        with st.expander("Current orders"):
            st.dataframe(df)
        list_of_orders = [i[0] for i in view_only_orders()]
        selected_order = st.selectbox("orders to Edit", list_of_orders)
        selected_result = get_order_id(selected_order)
        # st.write(selected_result)
        if selected_result:
            order_ID = selected_result[0][0]
            order_date = selected_result[0][1]
            delivery_date = selected_result[0][2]
            cust_ID = selected_result[0][3]
            dealer_ID = selected_result[0][4]
            
            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_order_ID = st.text_input("order_ID:",order_ID)
                new_order_date = st.text_input("order_date:", order_date)
                new_delivery_date = st.text_input("delivery_date:", delivery_date)

            with col2:
                new_cust_ID = st.text_input("cust_ID:",cust_ID)
                new_dealer_ID = st.text_input("dealer_ID:",dealer_ID)
                
                
            if st.button("Update order"):
                edit_orders_data(new_order_ID,new_order_date ,new_delivery_date ,new_cust_ID ,new_dealer_ID,order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID)
                st.success("Successfully updated:: {} to ::{}".format(order_ID, new_order_ID))

        result2 = view_all_orders()
        df2 = pd.DataFrame(result2, columns=['order_ID','order_date' ,'delivery_date' ,'cust_ID' ,'dealer_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
