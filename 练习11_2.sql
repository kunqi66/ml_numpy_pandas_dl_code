/*CREATE DATABASE test2_library;
USE test2_library;
CREATE TABLE books(
    b_id INT(11) UNIQUE KEY NOT NULL,
    b_name VARCHAR(50) NOT NULL,
    authors VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    pubdate YEAR NOT NULL,
    note VARCHAR(100),
    num int(11) NOT NULL
);
INSERT INTO books(b_id, b_name, authors,
price, pubdate, note, num)
VALUES(1,'毛选','毛泽东',23.8,1956,'sadad',5);*/

USE test2_library;
/*
INSERT INTO books VALUES(2,'马哲','马克斯',26.4,1986,'sadad',8);

INSERT INTO books VALUES(3,'孙子兵法','孙武',56.4,2003,'afada',10),
(4,'Story of Jane','Jane Tim',40,2001,'sadad',0),
(5,'Lovey Doy','George Byron',20,2005,'sadad',30);*/

UPDATE books SET price = price + 5
WHERE note = 'sadad';

UPDATE books SET price = 40
WHERE b_name = '毛选';

DELETE FROM books WHERE num = 0;





