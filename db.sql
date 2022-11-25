create table user_account(user_id varchar(10),
					fname varchar(15) NOT NULL,
                    lname varchar(15) NOT NULL,
                    dob varchar(30)  NOT NULL,
                    phone varchar(10) NOT NULL ,
                    email varchar(40) NOT NULL,
                    country varchar(20) NOT NULL,
					city varchar(30),
					pincode int(6),
                    bank_name varchar(20) NOT NULL,
                    primary key(user_id));

create table wallet(t_id varchar(20)  NOT NULL,
					user_id varchar(20)   NOT NULL,
					account_no varchar(20)  NOT NULL,
					bank_name varchar(30)   NOT NULL,
					balance int  check(balance > 0),
					promocode varchar(20)  default NULL,
					loan varchar(10) default NULL,
					primary key(t_id,user_id,promocode));

create table transactions(transaction_id varchar(10),
						transaction_date varchar(20),
						transaction_detail varchar(30),
						amount int check (amount>100),
						to_id varchar(20),
						from_id varchar(20),
						type_trans varchar(20),
						primary key(transaction_id,to_id,from_id));

create table promo_offers(promo_id varchar(10),
						user_id varchar(10),
						start_date varchar(20) NOT NULL,
						end_date varchar(20)  NOT NULL,
						duration varchar(20)  NOT NULL,
						status varchar(20)  NOT NULL,
						amount_value varchar(50) NOT NULL,
						primary key(promo_id,user_id),
                        FOREIGN KEY (user_id) REFERENCES user_account(user_id) ON DELETE CASCADE);

create table dependents(dependent_id varchar(10)  NOT NULL,
						trans_id varchar(10)  UNIQUE,
						user_ref_id varchar(20),
						fname varchar(20) NOT NULL,
						lname varchar(20) NOT NULL,
						phone varchar(10) NOT NULL,
						email varchar(50) NOT NULL,
						dob varchar(30) NOT NULL,
						relation varchar(20) NOT NULL UNIQUE,
						primary key(dependent_id,trans_id,user_ref_id));

create table transaction_status(trans_id varchar(10),
								u_id varchar(10),
								primary key (trans_id,u_id));



ALTER TABLE wallet
ADD CONSTRAINT FK_t_id
FOREIGN KEY (t_id) REFERENCES transactions(transaction_id)
ON DELETE CASCADE;

ALTER TABLE transaction_status
ADD CONSTRAINT FK_u_id
FOREIGN KEY (u_id) REFERENCES user_account(user_id)
ON DELETE CASCADE;

ALTER TABLE transaction_status
ADD status varchar(15);

ALTER TABLE transaction_status
ADD status varchar(15);

create table promo_offers_transactions(prom_id varchar(10),
						usr_id varchar(10),
						transactions_no int(10),
						duration int(20)  NOT NULL,
						amount_value int(20) NOT NULL,
						primary key(prom_id,usr_id));




