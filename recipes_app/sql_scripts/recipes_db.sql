CREATE DATABASE recipes_db;

USE recipes_db;

CREATE TABLE users(
	firstName VARCHAR(250) NOT NULL,
    secondName VARCHAR(250) NOT NULL,
    email VARCHAR(250) NOT NULL PRIMARY KEY,
    password VARCHAR(250) NOT NULL
);

CREATE TABLE recipes(
	rcp_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	rcp_name VARCHAR(250) NOT NULL,
    rcp_description VARCHAR(250) NOT NULL,
    rcp_instructions VARCHAR(250) NOT NULL,
    rcp_timemaking BOOL NOT NULL,
    rcp_date DATETIME (250) NOT NULL
);

INSERT INTO users(firstName, secondName, email, password)
VALUES( 'Javier', 'Mora', 'correo@gmail.com', 'pass123' ),
	  ( 'Laura', 'Mata', 'correo2@correo.com', 'pass456' );

INSERT INTO recipes(rcp_id, rcp_name, rcp_description, rcp_instructions, rcp_timemaking, rcp_date)
VALUES( 001, 'Hot Dog', 'Hot Dog Description', 'Hot Dog Instructions', FALSE, 10/05/2021 ),
	  ( 002, 'Taco', 'Taco Description', 'Taco Instructions', TRUE, 10/05/2021 );