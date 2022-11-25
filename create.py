import streamlit as st
from database import add_data_customer
from database import add_data_dealer
from database import add_data_admin
from database import add_data_orders


# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID


def create(table):
    if table=='customer':
        col1, col2 = st.columns(2)
        with col1:
            cust_id = st.text_input("cust_id:")
            name = st.text_input("name:")
            ph_no =  st.text_input("Ph_no:")
            address =  st.text_input("address:")

        with col2:
            email_id = st.text_input("email_id:")
            password = st.text_input("password:")
            pan_no = st.text_input("pan_no:")
            


        if st.button("Add data"):
            add_data_customer(cust_id,name,ph_no ,address ,email_id ,password ,pan_no)
            st.success("Successfully booked : {}".format(cust_id))

    elif table=='admin':
        col1, col2 = st.columns(2)
        with col1:
            admin_id = st.text_input("admin_id:")
            

        with col2:
            admin_password = st.text_input("admin_password:")
            
        if st.button("Add data"):
            add_data_admin(admin_id,admin_password)
            st.success("Successfully added : {}".format(admin_id))

# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID


    elif table == 'dealer':
        col1, col2 = st.columns(2)
        with col1:
            dealer_id = st.text_input("dealer_id:")
            name = st.text_input("name:")
            licence_no = st.text_input("licence_no:")
        with col2:
            location = st.text_input("location:")
            admin = st.text_input("admin:")

        if st.button("Add data"):
            add_data_dealer(dealer_id,name,licence_no,location,admin)
            st.success("Successfully added : {}".format(dealer_id))


    elif table == 'orders':
        col1, col2 = st.columns(2)
        with col1:
            order_id = st.text_input("order_id:")
            order_date = st.text_input("order_date:")
            delivery_date = st.text_input("delivery_date:")

            
        with col2:
            cust_id = st.text_input("cust_id:")
            dealer_id = st.text_input("dealer_id:")


        if st.button("Add data"):
            add_data_orders(order_id,order_date ,delivery_date ,cust_id ,dealer_id)

            st.success("Successfully added : {}".format(order_id))