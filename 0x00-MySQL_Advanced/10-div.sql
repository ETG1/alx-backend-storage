-- SQL script to create a function SafeDiv that performs division and handles division by zero

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)    
BEGIN
    DECLARE result DECIMAL(10, 2);  

  
    IF b = 0 THEN
        SET result = 0; 
    ELSE
        SET result = a / b;  
    END IF;

    RETURN result;
END$$

DELIMITER ;
