CREATE TABLE customer (
    Cust_ID int NOT NULL,
    Name varchar(25) NOT NULL,
    Ph_No varchar(25) NOT NULL,
    Address varchar(50) NOT NULL,
    email_ID varchar(25),
    password varchar(25),
    PAN_No varchar(25) NOT NULL,
    PRIMARY KEY (Cust_ID)
);


CREATE TABLE admin (
    Admin_ID int,
    admin_password varchar(25),
    PRIMARY KEY (Admin_ID)
);

CREATE TABLE Dealer (
    dealer_ID int NOT NULL,
    name varchar(25) NOT NULL,
    licence_no int,
    location varchar(50),
    admin int,
    PRIMARY KEY (dealer_ID),
    FOREIGN KEY (admin) REFERENCES admin(Admin_ID)
);

CREATE TABLE Orders (
    order_ID int NOT NULL,
    order_date date NOT NULL,
    delivery_date date,
    cust_ID int,
    dealer_ID int,
    PRIMARY KEY (order_ID),
    FOREIGN KEY (cust_ID) REFERENCES customer(cust_ID),
    FOREIGN KEY (dealer_ID) REFERENCES dealer(dealer_ID)
);


