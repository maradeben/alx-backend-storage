-- script that creates an index idx_first_name
-- on the table names and on the first letter of name and score

CREATE INDEX idx_first_name_score ON names (name(1), score);
