-- create trigger that decrements the qty of item
-- when an order is made

CREATE TRIGGER dec_item AFTER INSERT ON orders
	FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
