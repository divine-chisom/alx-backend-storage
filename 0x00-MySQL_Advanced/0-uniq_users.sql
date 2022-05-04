-- Creates a table with unique users.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NUll PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
