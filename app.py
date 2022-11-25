# Importing pakages
import streamlit as st
import mysql.connector
from create import create
from database import create_table
from database import query_1
from delete import delete
from read import read
from update import update
#from function import delete_orders_dealer
from join import join
from aggregate import agg
#from queries import execute_query
#from procedure import info_1

mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
c = mydb.cursor()

# c.execute("CREATE DATABASE pes1ug20cs062_final_project")
c.execute("use gas_v1")

def main():
    st.title("Gas Booking System")
    menu = ["Add", "View", "Edit", "Remove","Function","Join","Aggregate","Query"]
    table_names=["customer","admin","dealer","orders"]
    choice = st.sidebar.selectbox("action", menu)
    table=st.sidebar.selectbox("table", table_names)
    #create_table(table)
    if choice == "Add":
        if table=='customer':
            st.subheader("Enter customer Details:")
            create(table)
        elif table=='admin':
            st.subheader("Enter admin Details:")
            create(table)
        elif table=='dealer':
            st.subheader("Enter dealer Details:")
            create(table)
        elif table=='orders':
            st.subheader("Enter order Details:")
            create(table)


    if choice == "View":
        if table=='customer':
            st.subheader("View entered customer Details:")
            read(table)
        elif table=='admin':
            st.subheader("View entered admin Details:")
            read(table)
        elif table=='dealer':
            st.subheader("View dealer Details:")
            read(table)
        elif table=='orders':
            st.subheader("View entered orders Details:")
            read(table)
        
    
    if choice == "Remove":
        if table=='customer':
            st.subheader("Delete enetered customer Details:")
            delete(table)
        elif table=='admin':
            st.subheader("Delete entered admin Details:")
            delete(table)
        elif table=='dealer':
            st.subheader("Delete dealer:")
            delete(table)
        elif table=='orders':
            st.subheader("Delete entered order Details:")
            delete(table)
        

    if choice == "Edit":
        if table=='customer':
            st.subheader("Update entered customer Details:")
            update(table)
        elif table=='admin':
            st.subheader("Update entered admin Details:")
            update(table)
        elif table=='dealer':
            st.subheader("Update entered dealer Details:")
            update(table)
        elif table=='orders':
            st.subheader("Update entered order Details:")
            update(table)

    

    if choice=='Function':
        st.subheader("delete all orders for certain dealer_id")
        delete_orders_dealer()
    
    if choice=='Join':
        st.subheader("join:")
        join()

    if choice=='Aggregate':
        st.subheader("Aggregate:")
        agg()

    # if choice=='Query':
    #     st.subheader("Enter QUERY:")
    #     execute_query()

    # #if choice=='Procedure':
    # #    st.subheader("Information about customer:")
    # #    info_1()
    

    




if __name__ == '__main__':
    main()