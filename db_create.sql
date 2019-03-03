DROP DATABASE IF EXISTS sendit;
CREATE DATABASE  sendit;
\c sendit;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id serial PRIMARY KEY NOT NULL,
	email varchar(255)  NOT NULL default '',
	password varchar(255) NOT NULL,
	is_admin boolean NOT NULL);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	id serial PRIMARY KEY NOT NULL,
	item_name varchar(255) NOT NULL,
	sender varchar(255) NOT NULL,
	price real NOT NULL
);

INSERT INTO users (email, password, is_admin) VALUES ('manu', 'manu', FALSE);