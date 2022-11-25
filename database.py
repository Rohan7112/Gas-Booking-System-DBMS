# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="gas_v1"
)
c = mydb.cursor()


def create_table(table):

        c.execute('CREATE TABLE IF NOT EXISTS customer (Cust_ID int NOT NULL,Name varchar(25) NOT NULL,Ph_No varchar(25) NOT NULL,Address varchar(50) NOT NULL,email_ID varchar(25),password varchar(25),PAN_No varchar(25) NOT NULL,PRIMARY KEY (Cust_ID);')

        c.execute('CREATE TABLE IF NOT EXISTS admin (Admin_ID int,admin_password varchar(25),PRIMARY KEY (Admin_ID);')

        c.execute('CREATE TABLE IF NOT EXISTS CREATE TABLE Dealer (dealer_ID int NOT NULL,name varchar(25) NOT NULL,licence_no int,location varchar(50),admin int,PRIMARY KEY (dealer_ID),FOREIGN KEY (admin) REFERENCES admin(Admin_ID));')

        c.execute('CREATE TABLE IF NOT EXISTS Orders (order_ID int NOT NULL,order_date date NOT NULL,delivery_date date,cust_ID int,dealer_ID int,PRIMARY KEY (order_ID),FOREIGN KEY (cust_ID) REFERENCES customer(cust_ID),FOREIGN KEY (dealer_ID) REFERENCES dealer(dealer_ID));')


def add_data_customer(cust_id,name,ph_no ,address ,email_id ,password ,pan_no):
        c.execute('INSERT INTO customer(cust_id,name,ph_no ,address ,email_id ,password ,pan_no) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                  (cust_id,name,ph_no ,address ,email_id ,password ,pan_no))
        mydb.commit()

def add_data_admin(admin_id,admin_password):
        c.execute('INSERT INTO admin(admin_id,admin_password) VALUES (%s,%s)',
                  (admin_id,admin_password))
        mydb.commit()

def add_data_dealer(dealer_id,name,licence_no,location,admin):
        c.execute('INSERT INTO dealer(dealer_id,name,licence_no,location,admin) VALUES (%s,%s,%s,%s,%s)',
                  (dealer_id,name,licence_no,location,admin))
        mydb.commit()


def add_data_orders(order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID):
        c.execute('INSERT INTO orders(order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID) VALUES (%s,%s,%s,%s,%s)',
                  (order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID))
        mydb.commit()

#view tables
def view_all_customer():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data

def view_all_admin():
    c.execute('SELECT * FROM admin')
    data = c.fetchall()
    return data

def view_all_data_dealer():
    c.execute('SELECT * FROM dealer')
    data = c.fetchall()
    return data

def view_all_orders():
    c.execute('SELECT * FROM orders')
    data = c.fetchall()
    return data



#viewonly tables
def view_only_customer():
    c.execute('SELECT cust_id FROM customer')
    data = c.fetchall()
    return data
def view_only_admin():
    c.execute('SELECT admin_id FROM admin')
    data = c.fetchall()
    return data
def view_only_dealer():
    c.execute('SELECT dealer_id FROM dealer')
    data = c.fetchall()
    return data
def view_only_orders():
    c.execute('SELECT order_id FROM orders')
    data = c.fetchall()
    return data


#getting
def get_cust_id(cust_id):
    c.execute('SELECT * FROM customer WHERE cust_id="{}"'.format(cust_id))
    data = c.fetchall()
    return data
def get_admin_id(admin_id):
    c.execute('SELECT * FROM admin WHERE admin_id="{}"'.format(admin_id))
    data = c.fetchall()
    return data

def get_dealer_id(dealer_id):
    c.execute('SELECT * FROM dealer WHERE dealer_id="{}"'.format(dealer_id))
    data = c.fetchall()
    return data

def get_order_id(order_id):
    c.execute('SELECT * FROM orders WHERE order_id="{}"'.format(order_id))
    data = c.fetchall()
    return data

# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID

#editing
def edit_customer_data(new_cust_id,new_name,new_ph_no ,new_address ,new_email_id ,new_password ,new_pan_no ,cust_id,name,ph_no ,address ,email_id ,password ,pan_no):
    c.execute("UPDATE customer SET cust_id=%s,name=%s, ph_no=%s, address=%s, email_id=%s,password=%s,pan_no=%s WHERE "
              "cust_id=%s and name=%s and ph_no=%s and address=%s and email_id=%s and password=%s and pan_no=%s",(new_cust_id,new_name,new_ph_no ,new_address ,new_email_id ,new_password ,new_pan_no ,cust_id,name,ph_no ,address ,email_id ,password ,pan_no))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_admin_data(new_admin_id,new_admin_password,admin_id,admin_password_id):
    c.execute("UPDATE admin SET admin_id=%s, admin_password=%s WHERE "
              "admin_id=%s and admin_password=%s", (new_admin_id,new_admin_password,admin_id,admin_password_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_dealer_data(new_dealer_id,new_name,new_licence_no,new_location,new_admin,dealer_id,name,licence_no,location,admin):
    c.execute("UPDATE dealer SET dealer_id=%s,name=%s,licence_no=%s,location=%s,admin=%s WHERE "
              "dealer_id=%s and name=%s and licence_no=%s and location=%s and admin=%s  ", (new_dealer_id,new_name,new_licence_no,new_location,new_admin,dealer_id,name,licence_no,location,admin))
    mydb.commit()
    data = c.fetchall()
    return data


def edit_orders_data(new_order_ID,new_order_date ,new_delivery_date ,new_cust_ID ,new_dealer_ID,order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID):
    c.execute("UPDATE orders SET order_ID=%s,order_date=%s ,delivery_date=%s ,cust_ID=%s ,dealer_ID=%s WHERE "
              "order_ID=%s and order_date=%s and delivery_date=%s and cust_ID=%s and dealer_ID=%s ", (new_order_ID,new_order_date ,new_delivery_date ,new_cust_ID ,new_dealer_ID,order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID))
    mydb.commit()
    data = c.fetchall()
    return data

# cust_id,name,ph_no ,address ,email_id ,password ,pan_no
# admin_id,admin_password
# dealer_id,name,licence_no,location,admin
# order_ID,order_date ,delivery_date ,cust_ID ,dealer_ID
#delete
def delete_customer(cust_id):
    c.execute('DELETE FROM customer WHERE cust_id="{}"'.format(cust_id))
    mydb.commit()

def delete_admin(admin_id):
    c.execute('DELETE FROM admin WHERE admin_id="{}"'.format(admin_id))
    mydb.commit()

def delete_dealer(dealer_id):
    c.execute('DELETE FROM dealer WHERE dealer_id="{}"'.format(dealer_id))
    mydb.commit()

def delete_order(order_id):
    c.execute('DELETE FROM orders WHERE order_id="{}"'.format(order_id))
    mydb.commit()

def loan(x):
    c.execute('SELECT loan({})'.format(x))
    data = c.fetchall()
    return data


def joining():
    c.execute('SELECT orders.order_id,dealer.name FROM orders JOIN dealer ON orders.dealer_id = dealer.dealer_id;')
    data = c.fetchall()
    return data

def joining_2():
    c.execute('SELECT orders.order_id,customer.address FROM orders JOIN customer ON orders.cust_id= customer.cust_id;')
    data = c.fetchall()
    return data

def joining_3():
    c.execute('SELECT dealer.dealer_id, dealer.name,admin.admin_id,admin.admin_password FROM dealer JOIN admin ON dealer.admin= admin.admin_id')
    data = c.fetchall()
    return data



def aggregate():
    c.execute('SELECT delivery_date, COUNT(delivery_date) FROM orders GROUP BY delivery_date;')
    data = c.fetchall()
    return data

def aggregate_2():
    c.execute('SELECT location, count(location) FROM dealer GROUP BY location;')
    data = c.fetchall()
    return data

def aggregate_3():
    c.execute('SELECT admin_id, count(admin_id) FROM dealer JOIN admin ON dealer.admin= admin.admin_id')
    data = c.fetchall()
    return data



def query_1(x):
    c.execute(x)
    data = c.fetchall()
    return data






