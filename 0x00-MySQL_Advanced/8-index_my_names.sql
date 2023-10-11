-- script that creates an index idx_first_name
-- on the table names and on the first letter of name

CREATE INDEX idx_first_name ON names (name(1));
