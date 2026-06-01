/*CREATE DATABASE test01_market;

USE test01_market;
CREATE TABLE customers(
    c_num INT(11),
    c_name VARCHAR(50),
    c_contact VARCHAR(50),
    c_city VARCHAR(50),
    c_birth date
);*/

/*ALTER TABLE customers MODIFY c_contact VARCHAR(50)
AFTER c_birth;

ALTER TABLE customers MODIFY  c_name VARCHAR(70);

ALTER TABLE customers CHANGE c_contact c_phone VARCHAR(50);*/
/*
ALTER TABLE customers ADD c_gender char(1) AFTER c_name;*/
/*
ALTER TABLE customers RENAME to customers_info;*/

ALTER TABLE customers_info DROP COLUMN c_city