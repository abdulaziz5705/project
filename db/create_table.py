from main import Database


def create_table():
    country = f"""
        CREATE TABLE country (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50));
    """
    city = f"""
           CREATE TABLE city (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               country_id INT REFERENCES country(id));
       """
    address = f"""
           CREATE TABLE address (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               city_id INT REFERENCES city(id));
       """
    category = f"""
           CREATE TABLE category (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               create_date TIMESTAMP DEFAULT  now());
       """
    store = f"""
           CREATE TABLE store (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               star_count INT,
               open_date INT,
               address_id INT REFERENCES address(id),
               create_date TIMESTAMP DEFAULT now());
       """
    customer = f"""
           CREATE TABLE customer (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               last_name VARCHAR(50),
               years_old INT,
               phone_number integer,
               address_id INT REFERENCES address(id),
               username VARCHAR(100),
               password VARCHAR(100),
               create_date TIMESTAMP DEFAULT now());
               
       """
    product = f"""
           CREATE TABLE product (
               id SERIAL PRIMARY KEY,
               name VARCHAR(50),
               price INT,
               count INT,
               start_date INT,
               end_date INT,
               star_count INT,
               serial_number smallint,
               store_id  INT REFERENCES address(id),
               categoty_id INT REFERENCES category(id),
               create_date TIMESTAMP DEFAULT now());
       """
    order = f"""
           CREATE TABLE order (
               id SERIAL PRIMARY KEY,
              product_id INT REFERENCES product(id),
              customer_id INT REFERENCES  customer(id),
              amount INT,
              create_date TIMESTAMP DEFAULT now()); """
    data = {"country": country,
            "city": city,
            "category": category,
            "address": address,
            "store": store,
            "customer": customer,
            "product": product,
            "order": order}
    for i in data:
            #print(i)
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()
