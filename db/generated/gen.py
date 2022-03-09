from werkzeug.security import generate_password_hash
import csv
import random
import numpy as np
from faker import Faker
import os

num_users = 1000
num_products = 2000
num_purchases = 2500
num_sellers = 100
reviews_per = 20
users_with_carts = 200

Faker.seed(0)
fake = Faker()


def get_csv_writer(f):
    return csv.writer(f, dialect='unix')


def gen_users(num_users):
    userEmails = []
    with open('Users.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Users...', end=' ', flush=True)
        for uid in range(num_users):
            if uid % 10 == 0:
                print(f'{uid}', end=' ', flush=True)
            profile = fake.profile()
            email = profile['mail']
            if email in userEmails:
                eList = email.split("@")
                eList[0] = eList[0] + str(fake.random_int(max=1000))
                email = "@".join(eList)
            userEmails.append(email)
            plain_password = f'pass{uid}'
            password = generate_password_hash(plain_password)
            name_components = profile['name'].split(' ')
            firstname = name_components[0]
            lastname = name_components[-1]
            addr = profile['address']
            balance = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            writer.writerow([uid, email, password, firstname, lastname, addr, balance])
        print(f'{num_users} generated')
    return
def gen_sellers(num_sellers):
    with open('Sellers.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Sellers...', end = ' ', flush = True)
        for uid in range(num_sellers):
            if uid % 100 == 0:
                print(f'{uid}', end = ' ', flush=True)
            writer.writerow([uid])
        print(f'{num_sellers} generated')
    return

def gen_products(num_products):
    available_pids = []
    with open("product_names.npy","rb") as f:
        names = np.load(f,allow_pickle=1) 
    np.random.shuffle(names)
    with open('Products.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Products...', end=' ', flush=True)
        for pid in range(num_products):
            if pid % 100 == 0:
                print(f'{pid}', end=' ', flush=True)
            name = names[pid]
            category = fake.random_element(elements=('Food','Drinks','Art','random'))
            available = fake.random_element(elements=('true', 'false'))
            description_link = fake.random_element(elements = ('!',str(pid)))
            if available == 'true':
                available_pids.append(pid)
            writer.writerow([pid, name, category, available, description_link])
        print(f'{num_products} generated; {len(available_pids)} available')
    return available_pids

def gen_inventory(available_pids, sellers_per_product):
    product_quantity = {}
    product_seller = {}
    ret = []
    with open('Inventory.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Inventory ...', end = ' ', flush = True)
        for product in available_pids:
            for s in range(sellers_per_product):
                seller_id = fake.random_int(min = 0, max = num_sellers-1)
                while (product in product_seller.keys()) and (seller_id in product_seller.get(product)):
                    seller_id = fake.random_int(min = 0, max = num_sellers-1)
                quantity = fake.random_int(min = 1, max = 300)
                price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
                product_quantity.update({product : quantity})
                if product not in product_seller.keys():
                    e = []
                    product_seller.update({product : e})
                product_seller.get(product).append(seller_id)
                writer.writerow([product, seller_id, price, quantity])
    print('generated!')
    ret.append(product_quantity)
    ret.append(product_seller)
    return ret

def gen_purchases(num_purchases):
    users_orders = {}
    with open('Orders.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Purchases...', end=' ', flush=True)
        for id in range(num_purchases):
            if id % 100 == 0:
                print(f'{id}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            time_purchased = fake.date_time()
            users_orders.update({id : uid})
            writer.writerow([id, uid, time_purchased])
        print(f'{num_purchases} generated')
    return users_orders

def gen_items_ordered(num_purchases, product_seller, available_pids):
    orders_items = {}
    with open('Items_Ordered.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Items Ordered ...', end=' ', flush = True)
        for order_id in range(num_purchases):
            if order_id % 100 == 0:
                print(f'{order_id}', end= ' ', flush = True)
            product_id = fake.random_element(elements = available_pids)
            seller_id = random.choice(product_seller.get(product_id))
            price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            quantity = fake.random_int(min = 1, max = 20)
            status = fake.random_int(min = 0, max = 1)           
            fulfillment_time = fake.date_time()
            orders_items.update({order_id : product_id})
            writer.writerow([order_id, product_id, seller_id, price, quantity, status, fulfillment_time])
        print(f'{num_purchases} generated')
    return orders_items

def create_user_product_dictionary(users_orders, orders_items): 
    user_product = {}
    for order_id in users_orders: 
        user_id = users_orders.get(order_id)
        product_id = orders_items.get(order_id)
        user_product.update({user_id : product_id})
    return user_product

def gen_product_ratings(user_product, product_seller):
    with open("reviews.npy","rb") as f:
        reviews = np.load(f,allow_pickle=1)
    with open('Product_Ratings.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Product Ratings ...', end = ' ', flush = True)
        for counter, user_id in enumerate(user_product):
            product_id = user_product.get(user_id)
            seller_id = random.choice(product_seller.get(product_id))
            rating = fake.random_int(min = 0, max = 5)
            review = reviews[counter]
            review_time = fake.date_time()
            writer.writerow([product_id, seller_id, user_id, rating, review,review_time])
        print(f'{num_purchases} generated')
        return
def gen_seller_ratings(reviews_per):
    with open('Seller_Ratings.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Seller Ratings ...', end = ' ', flush = True)
        for seller_id in range(num_sellers):
            reviewers = []
            for rev in range(reviews_per):
                buyer_id = fake.random_int(min = 0, max = num_users-1)
                while buyer_id in reviewers:
                    buyer_id = fake.random_int(min = 0, max = num_users-1)
                reviewers.append(buyer_id)
                rating = fake.random_int(min = 0, max = 5)
                review = fake.sentence(nb_words=20)[:-1]
                review_time = fake.date_time()
                writer.writerow([seller_id, buyer_id, rating, review, review_time])
        print(f'{num_sellers * reviews_per} generated')
        return

def gen_cart(product_quantity, product_seller, users_with_carts):
    with open('Cart.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Cart ...', end = ' ', flush = True)
        for cart in range(users_with_carts):
            for item_in_cart in range(fake.random_int(min = 0, max = 5)):
                user_id = fake.random_int(min = 0, max = num_users-1)
                product_id = random.choice(list(product_quantity.keys()))
                seller_id = random.choice(product_seller.get(product_id))
                quantity = 1 #fake.random_int(min = 1, max = product_quantity.get(product_id))
                writer.writerow([user_id, product_id, seller_id, quantity])
    print(f'{users_with_carts} carts generated')
    return

def gen_descriptions(available_pids):
    for pid in available_pids:
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if os.path.exists(path+"/data/descriptions/"+str(pid)+".txt"):
            os.remove(path+"/data/descriptions/"+str(pid)+".txt")
        
        with open(path+"/data/descriptions/"+str(pid)+".txt", "a+") as f:
            f.write(fake.sentence(nb_words=20)[:-1])

    return
#gen_users(num_users)
gen_sellers(num_sellers)
available_pids = gen_products(num_products)
ret = gen_inventory(available_pids, 4)
product_quantity = ret[0]
product_seller = ret[1]
gen_cart(product_quantity, product_seller, users_with_carts)
users_orders = gen_purchases(num_purchases)
orders_items = gen_items_ordered(num_purchases, product_seller, available_pids)
user_product = create_user_product_dictionary(users_orders, orders_items)
gen_product_ratings(user_product, product_seller)
gen_seller_ratings(reviews_per)
gen_descriptions(available_pids)
