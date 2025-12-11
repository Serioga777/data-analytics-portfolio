-- SQL Customer Behavior Analysis Project
-- Database: customer_analytics

-- Create tables
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT UNIQUE,
    join_date DATE,
    country TEXT,
    customer_segment TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample customers
INSERT INTO customers VALUES
(1, 'John Smith', 'john.smith@email.com', '2023-01-15', 'UK', 'Premium'),
(2, 'Sarah Johnson', 'sarah.j@email.com', '2023-02-20', 'UK', 'Standard'),
(3, 'Michael Brown', 'mbrown@email.com', '2023-03-10', 'USA', 'Premium'),
(4, 'Emma Wilson', 'emma.w@email.com', '2023-04-05', 'UK', 'Standard'),
(5, 'David Lee', 'david.lee@email.com', '2023-05-12', 'Canada', 'Premium'),
(6, 'Lisa Taylor', 'lisa.t@email.com', '2023-06-18', 'UK', 'Basic'),
(7, 'James Anderson', 'james.a@email.com', '2023-07-22', 'USA', 'Standard'),
(8, 'Sophie Martin', 'sophie.m@email.com', '2023-08-30', 'UK', 'Premium'),
(9, 'Robert Garcia', 'robert.g@email.com', '2023-09-14', 'USA', 'Basic'),
(10, 'Emily Clark', 'emily.c@email.com', '2023-10-28', 'Canada', 'Standard');

-- Insert sample products
INSERT INTO products VALUES
(1, 'Premium Subscription', 'Services', 99.99),
(2, 'Basic Subscription', 'Services', 29.99),
(3, 'Advanced Analytics', 'Tools', 149.99),
(4, 'Data Export Tool', 'Tools', 49.99),
(5, 'Custom Reports', 'Reports', 79.99);

-- Insert sample orders
INSERT INTO orders VALUES
(1, 1, '2024-01-10', 99.99, 'Completed'),
(2, 1, '2024-02-15', 149.99, 'Completed'),
(3, 2, '2024-01-20', 29.99, 'Completed'),
(4, 3, '2024-01-25', 99.99, 'Completed'),
(5, 4, '2024-02-01', 29.99, 'Completed'),
(6, 5, '2024-02-10', 199.98, 'Completed'),
(7, 6, '2024-02-14', 29.99, 'Cancelled'),
(8, 7, '2024-03-01', 49.99, 'Completed'),
(9, 8, '2024-03-05', 249.98, 'Completed'),
(10, 9, '2024-03-10', 29.99, 'Completed'),
(11, 10, '2024-03-15', 79.99, 'Completed'),
(12, 1, '2024-03-20', 99.99, 'Completed'),
(13, 3, '2024-03-22', 149.99, 'Completed'),
(14, 5, '2024-03-25', 99.99, 'Completed'),
(15, 8, '2024-03-28', 99.99, 'Completed');

-- Insert order items
INSERT INTO order_items VALUES
(1, 1, 1, 1, 99.99),
(2, 2, 3, 1, 149.99),
(3, 3, 2, 1, 29.99),
(4, 4, 1, 1, 99.99),
(5, 5, 2, 1, 29.99),
(6, 6, 1, 2, 99.99),
(7, 7, 2, 1, 29.99),
(8, 8, 4, 1, 49.99),
(9, 9, 1, 1, 99.99),
(10, 9, 3, 1, 149.99),
(11, 10, 2, 1, 29.99),
(12, 11, 5, 1, 79.99),
(13, 12, 1, 1, 99.99),
(14, 13, 3, 1, 149.99),
(15, 14, 1, 1, 99.99),
(16, 15, 1, 1, 99.99);
