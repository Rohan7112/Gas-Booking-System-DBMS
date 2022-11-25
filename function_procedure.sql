DELIMITER //
CREATE procedure except_dealer_orders(IN x int)
BEGIN
	select * from dealer where dealer_id !=x;
end 
//
DELIMITER ;


DELIMITER //
CREATE function (x int)
BEGIN
	select * from dealer where dealer_id !=x;
end 
//
DELIMITER ;


DELIMITER $$
CREATE TRIGGER count_of_orders
BEFORE INSERT
ON orders FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
declare count int;
SET error_msg = ('number of orders per customer exceeding two');
IF (select count(cust_id) from orders where cust_id = new.cust_id) > 2 THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_msg;
END IF;
END
$$ 
DELIMITER ;