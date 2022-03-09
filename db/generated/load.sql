\COPY Product_Categories FROM 'Product_Categories.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Users FROM 'Users.csv' WITH DELIMITER ',' NULL '' CSV
SELECT pg_catalog.setval('public.users_id_seq', 1000, false);
\COPY Sellers FROM 'Sellers.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Products FROM 'Products.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Orders FROM 'Orders.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Inventory FROM 'Inventory.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Seller_ratings FROM 'Seller_Ratings.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Product_ratings FROM 'Product_Ratings.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Items_ordered FROM 'Items_Ordered.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Cart FROM 'Cart.csv' WITH DELIMITER ',' NULL '' CSV