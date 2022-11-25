/* FUNCTIONS*/
DELIMITER $$
CREATE FUNCTION `loan`(balance int) RETURNS varchar(50)
    DETERMINISTIC
BEGIN
DECLARE VALUE varchar(50);

IF balance<10000 then
set VALUE="Cannot apply for loan";

ELSE
set VALUE ="Can apply for loan";

end if;

return value;
END$$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION loan(balance int)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN/PES1UG20CS062/
DECLARE VALUE varchar(50);


DELIMITER $$
IF balance<10000 then
CREATE FUNCTION loan(balance int)
set VALUE="Cannot apply for loan";
RETURNS VARCHAR(50)

DETERMINISTIC
ELSE
BEGIN
set VALUE ="Can apply for loan";
DECLARE VALUE varchar(50);


end if;
IF balance<10000 then

set VALUE="Cannot apply for loan";
return value;

END;
ELSE
$$
set VALUE ="Can apply for loan";
DELIMITER ;


end if;
select user_id,loan(balance) as Validate

from wallet;
return value;

END;

$$

DELIMITER ;

select loan(2000);

/* PROCEDURES */
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `info`()
BEGIN
SELECT fname,lname,email FROM user_account;
end$$
DELIMITER ;

/*CURSORS:*/

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `createEmailList`(
	INOUT emailList varchar(4000)
)
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE emailAddress varchar(100) DEFAULT "";

	
	DEClARE curEmail 
		CURSOR FOR 
			SELECT email FROM user_account;

	
	DECLARE CONTINUE HANDLER 
        FOR NOT FOUND SET finished = 1;

	OPEN curEmail;

	getEmail: LOOP
		FETCH curEmail INTO emailAddress;
		IF finished = 1 THEN 
			LEAVE getEmail;
		END IF;
		
		SET emailList = CONCAT(emailAddress,";",emailList);
	END LOOP getEmail;
	CLOSE curEmail;

END$$
DELIMITER ;

/* TRIGGERS*/

CREATE TRIGGER `interest_add` BEFORE UPDATE ON `wallet`
 FOR EACH ROW BEGIN
      IF (NEW.balance > 10000) THEN
            SET NEW.balance = NEW.balance+(NEW.balance*0.2);
      ELSE
            SET NEW.balance = NEW.balance+(NEW.balance*0.2);
      END IF;
    END

/*JOIN*/



SELECT transactions.transaction_id, transaction_status.u_id,transactions.to_id, transactions.from_id, transaction_status.status
FROM transactions JOIN transaction_status
ON transaction_status.trans_id= transactions.transaction_id

SELECT transactions.transaction_id, transactions.type_trans,transactions.transaction_detail, dependents.dependent_id, dependents.relation
FROM transactions JOIN dependents
ON dependents.user_ref_id= transactions.transaction_id

SELECT user_account.user_id, user_account. fame, user_account. Iname, user_account.bank_name, wallet.balance, wallet. loan
FROM user account JOIN wallet
ON user_account.user_id= wallet.user_id


/*AGGREGATE*/
SELECT bank_name, COUNT (bank_name)
FROM user account GROUP BY bank name

SELECT to_id, SUM (amount)
FROM transactions
GROUP BY to_id;

SELECT bank_name, ROUND (AVG (BALANCE), 0) avg_balance
FROM wallet
GROUP BY bank name
ORDER BY bank_name;

SELECT user_account. fame, MAX(balance) highest_balance
FROM user account
INNER JOIN wallet USING (user_id);

/*SET*/

SELECT user_id, bank_name FROM user_account
UNION
SELECT user_id, bank_name FROM wallet;

SELECT t id as transaction id FROM wallet
UNION ALL
SELECT transaction_id FROM transactions;

SELECT bank name
FROM user account
WHERE country = 'India'
INTERSECT
SELECT bank name
FROM user account
WHERE country = 'America'

SELECT user id
FROM wallet
EXCEPT
SELECT user ref id
FROM dependents;


/*QUERY IN CLASS WHICH WAS GIVEN:-*/

SELECT from_id, COUNT(DISTINCT from_id) AS COUNT into @var1 FROM transactions GROUP BY from_id;

SELECT @someVariable := COUNT(DISTINCT from_id) FROM transactions GROUP BY from_id;


DELIMITER &&
CREATE TRIGGER `increase_date` BEFORE UPDATE ON `promo_offers_transactions`
FOR EACH ROW BEGIN
     IF (NEW.transactions.no > 9) THEN
           SET NEW.duration = NEW.duration+10;
     ELSE
           SET NEW.duration = NEW.duration-0;
     END IF;
END&&
DELIMETER ;
