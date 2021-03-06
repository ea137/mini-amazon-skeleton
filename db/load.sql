\COPY Users FROM 'data/Users.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Product_Categories FROM 'data/Categories.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Sellers FROM 'data/Sellers.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Products FROM 'data/Products.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Orders FROM 'data/Orders.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Inventory FROM 'data/Inventory.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Seller_ratings FROM 'data/Seller_ratings.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Product_ratings FROM 'data/Product_ratings.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Items_ordered FROM 'data/Items_ordered.csv' WITH DELIMITER ',' NULL '' CSV
\COPY Cart FROM 'data/Cart.csv' WITH DELIMITER ',' NULL '' CSV