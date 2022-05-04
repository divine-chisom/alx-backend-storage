-- Creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DROP TRIGGER IF EXISTS email_checker;
DELIMITER $$
CREATE TRIGGER email_checker
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;
