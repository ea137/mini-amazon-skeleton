Requirements (found in requirements.txt) and should be installed automatically when install.sh is run:
Nltk
Numpy
Sklearn
Pickle




Users Guru: Toni Iuzzolino
Displayed more information on the profile page. Allowed users to edit their information (except ID) and change their password. Implemented functionality for users to withdraw from their balance (up to their current balance). Created public views for users and sellers. Moved purchase history to the profile page and displayed information related to each purchase. Implemented functionality for users to search their purchase history by product name and sort it by product name, item price, and purchase time.


Products Guru: Will Strong
Added search functionality, including searching by category, name of product, and keywords in product name and description. Added functionality to sort by price ascending and descending. Added handling for product descriptions and viewing product descriptions. Enabled ability to search literally if query happens to be a category. Added descriptions to products. Ensured pagination was compatible with search.


Carts Guru: Ellie Angle
Added functionality for users to move items from cart into saved items, and from saved items into cart. Users can also increase the quantity of an item in their cart (up to the point that it matches current inventory). When a user places an order, the quantity they purchased is removed from a seller’s inventory. Altered styling for the cart page to reflect better usability. Adjusted database schema such that a product is sold by multiple sellers; when a user wants to add a product to cart, they choose from a variety of sellers at different price points. Added pagination for products page for increased usability.


Sellers Guru: Joe Cusano
Finished inventory page by adding buttons for quantity changes, price changes, and adding new products. Also fixed bugs with existing forms by creating new validators. Created orders page where users can view their orders, sort through them, search them, and mark orders as fulfilled. Modified install.sh and created new setup.sh to utilise new generated data during setup. Added a visualization where sellers can view their top selling products and compare them. Added a search and sort functionality to the inventory page.


Social Guru: Elarbi Amraoui
Added rating/review features for sellers. Added links in appropriate places in the website. Added a sort by feature for the reviews. Produced summary ratings for products and sellers (average rating and number of ratings). Additional features: basic ML model to predict the polarity (positive/negative) of the reviews (originally trained on a different dataset so the accuracy is not optimal; that said, it just needs to be re-trained and uploaded as a pickle file/ I have been working on a better Bert model, but the size of the model (500MB) is a limitation); ability to view only negative/positive reviews; ability to list reviews (products/sellers) for every single user.


Our github repository: https://gitlab.oit.duke.edu/ega12/mini-amazon-skeleton
Run ./setup.sh (in ~/mini-amazon-skeleton/db/generated). 
In total we have: 
* 1000 users
* 2500 orders
* 2000 products
* 915 product reviews
* 2000 seller reviews
* 100 sellers
* 4 product categories
* 2500 items ordered
