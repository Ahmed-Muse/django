DELIMITER //
DROP TRIGGER IF EXISTS after_allifmaalerpsystem_allifmaalstocktable_update//
CREATE TRIGGER after_allifmaalerpsystem_allifmaalstocktable_update AFTER UPDATE ON allifmaalerpsystem_allifmaalstocktable FOR EACH ROW
BEGIN
	IF new.issue_quantity = 0 
		THEN INSERT INTO allifmaalerpsystem_allifmaalstockhistorytable(
			id, 
			last_updated, 
			part_number, 
			description, 
			quantity_in_store, 
			receive_quantity, 
			receive_by) 
		VALUES(
			new.id, 
			new.last_updated, 
			new.part_number, 
			new.description, 
			new.quantity_in_store, 
			new.receive_quantity, 
			new.receive_by);

	ELSEIF new.receive_quantity = 0 
		THEN INSERT INTO allifmaalerpsystem_allifmaalstockhistorytable(
			id, 
			last_updated, 
			part_number, 
			description, 
			issue_quantity, 
			issue_to, 
			issue_by, 
			quantity_in_store) 
		VALUES(
			new.id, 
			new.last_updated, 
			new.part_number, 
			new.description, 
			new.issue_quantity, 
			new.issue_to, 
			new.issue_by, 
			new.quantity_in_store);
	END IF;
END//
DELIMITER ;