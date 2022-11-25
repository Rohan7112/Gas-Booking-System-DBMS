delete from user_account;
delete from wallet;
delete from transactions;
delete from promo_offers;
delete from user_details;
delete from dependents;
delete from login_credentials;
delete from transaction_status;
delete from password;

insert into user_account values ('VB201701','Vishal','Khanna','15-03-1979','9912121212','vishalkhanna@yahoo.com','India','Chandigarh','123456','State Bank Of India');
insert into user_account values ('VB201702','Anuj','Bhushan','05-06-1996','8197765465','anujbhushan5@gmail.com','India','Bangalore','123890','State Bank Of India');
insert into user_account values ('VB201703','Aniket','Bharati','11-01-1997','8147364941','bharatianiket@gmail.com','India','Bangalore','123890','Union Bank Of India');
insert into user_account values ('VB201704','Ankit','Reddy','11-02-1997','8179949418','hdreddy97@gmail.com','America','New York','123890','State Bank Of India');

insert into user_account values ('VB201705','Shreya','Narayan','11-09-1996','9913131313','narayanshreya@yahoo.com','India','Mangalore','123476','Axis Bank');
insert into user_account values ('VB201706','Dilip','Joshi','01-01-1980','9914141414','dilipjoshi@yahoo.com','India','Delhi','123019','Axis Bank');


/*insert into wallet values('T-220001','VB201701','SBIN201701','State Bank Of India',7500,'','');*/
insert into wallet values('T-220002','VB201702','SBIN201702','State Bank Of India',24500,'VB_MAR','');
insert into wallet values('T-220003','VB201703','UBIN201703','State Bank Of India',6000,'VB_MAR','1200');
insert into wallet values('T-220004','VB201704','ICIN201704','ICICI Bank Of India',50000,'VB_MAR','');
insert into wallet values('T-220005','VB201705','AXIN201705','Axis Bank Of India',9500,'','5000');

insert into wallet values('T-220006','VB201706','AXIN201706','Axus Bank Of India',1000,'','2000');


insert into transactions values('T-220002','22-03-2017','Transfer to Brother','50000','VB201705','VB201702','Wallet Transfer');
insert into transactions values('T-220003','22-03-2017','Transfer to Friend','20000','VB201704','VB201703','NEFT Transfer');
insert into transactions values('T-220004','15-03-2017','Transfer to Friend','50000','VB201702','VB201704','Wallet Transfer');
insert into transactions values('T-220005','16-03-2017','Transfer to Friend','9000','VB201704','VB201705','NEFT Transfer');


insert into transaction_status values('T-220002','VB201702','Completed');
insert into transaction_status values('T-220003','VB201703','Failed');


insert into promo_offers values('VB_MAR','VB201702','01-03-2017','31-03-2017','30 days','Active','Rs. 1000 V_Credit');
insert into promo_offers values('VB_MAR','VB201703','01-03-2017','31-03-2017','30 days','Active','Rs. 1000 V_Credit');
insert into promo_offers values('VB_MAR','VB201704','01-03-2017','31-03-2017','30 days','Active','Rs. 1000 V_Credit');


insert into dependents values('VBDP001','T-210002','T-220002','Virat','Kohli','8812121212','vkohli87@gmail.com','20-01-1987','Brother');
insert into dependents values('VBDP002','T-210004','T-220004','Neha','Krishna','8814141414','krihna_neha97@rediffmail.com','20-02-1987','Wife');
insert into dependents values('VBDP003','T-210005','T-220005','Vaibhav','Bhushan','8815151515','vaibhav_born99@gmail.com','20-03-1980','Brother In Law');

DELIMITER $$

    CREATE TRIGGER interest_add BEFORE UPDATE ON `wallet`
    FOR EACH ROW BEGIN
      IF (NEW.balance > 10000) THEN
            SET NEW.balance = NEW.balance+(NEW.balance*0.2);
      ELSE
            SET NEW.balance = NEW.balance+(NEW.balance*0.2);
      END IF;
    END$$

DELIMITER ;

