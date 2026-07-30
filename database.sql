CREATE DATABASE expensetracker1;
USE expensetracker1;
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(30) NOT NULL,
    amount DECIMAL(10,2) NOT NULL
);
DESCRIBE expenses;
SELECT * FROM expenses;