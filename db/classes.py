from main import Database


class Country:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def     select():
        query = "SELECT * FROM country ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
        INSERT INTO country(name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"UPDATE country SET {column} = {new_name} WHERE {column} = {old_name}"

        else:
            query = f"UPDATE country SET {column} = '{new_name}' WHERE {column} = '{old_name}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, date):
        if column == "id":
            query = f"DELETE FROM country WHERE {column} = {date}"
        else:
            query = f"DELETE FROM country WHERE {column} ='{date}'"
        return Database.connect(query, "delete")


class City:
    def __init__(self, name: str, country_id: int):
        self.name = name
        self.country_id = country_id

    @staticmethod
    def select():
        query = "SELECT c.name, s.name as Countryid FROM city c INNER JOIN country s ON c.country_id=s.id"
        data = Database.connect(query, "select")


    @staticmethod
    def insert(name, country_id):
        query = f"INSERT INTO city(name, country_id) VALUES ('{name}',  {country_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column: str, new_date: str, old_date: str):
        if column == "id":
            query = f"UPDATE city SET {column} = {new_date} WHERE {column} = {old_date}"
        else:
            query = f"UPDATE city SET {column} = '{new_date}' WHERE {column} = '{old_date}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column: str, new_name: str):
        if column == "id":
            query = f"DELETE FROM city WHERE {column} = {new_name}"
        else:
            query = f"DELETE FROM city WHERE {column} = '{new_name}'"
        return Database.connect(query, "delete")


class Address:
    def __init__(self, name, city_id):
        self.id = id
        self.name = name
        self.city_id = city_id

    @staticmethod
    def select():
        query = "SELECT a.name, c.name as Cityid FROM address a INNER JOIN city c ON a.city_id = c.id"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
            Name: {i[0]}
            City id: {i[1]}
            """)

    def insert(self):
        query = f"INSERT INTO address(name, city_id) VALUES ('{self.name}', {self.city_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column: str, new_date: str, old_date: str):
        if column == "id":
            query = f"UPDATE address SET {column} = '{new_date}' WHERE {column} = {old_date}'"

        else:
            query = (f"UPDATE address SET {column} = '{new_date}' WHERE {column} = '{old_date}'"
                     f"")
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM address WHERE {column} = {name}"
        else:
            query = f"DELETE FROM address WHERE {column} = '{name}'"
        return Database.connect(query, "delete")


class Category:
    def __init__(self, name):
        #self.id = id
        self.name = name

    @staticmethod
    def select():
        query = "SELECT * FROM category"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"INSERT INTO category(name) VALUES('{self.name}')"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, date, old_date):
        if column == "id":
            query = f"UPDATE category SET {column} = {date} WHERE {column} = {old_date}'"

        else:
            query = f"UPDATE category SET {column} = '{date}' WHERE {column} = '{old_date}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM category WHERE {column} = {name}"
        else:
            query = f"DELETE FROM category WHERE {column} = '{name}'"
        return Database.connect(query, "delete")


class Store:
    def __init__(self, name, star_count, open_date, address_id):
        self.name = name
        self.star_count = star_count
        self.open_date = open_date
        self.address_id = address_id

    @staticmethod
    def select():
        query = "SELECT s.name, s.star_count,s.open_date, a.name as Addressid FROM store s INNER JOIN address a ON s.address_id=a.id"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
            Name: {i[0]}
            Star count: {i[1]}
            Open date: {i[2]}
            Address id: {i[3]}
            """)

    def insert(self):
        query = f"INSERT INTO store(name, star_count, open_date, address_id) VALUES('{self.name}', '{self.star_count}', {self.open_date}, {self.address_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"UPDATE store SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"UPDATE store SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM store WHERE {column} = {name}"
        else:
            query = f"DELETE FROM store WHERE {column} = '{name}'"
        return Database.connect(query, "delete")


class Customer:
    def __init__(self, name, last_name, years_old, phone_number, username, password):

        self.name = name
        self.last_name = last_name
        self.years_old = years_old
        self.phone_number = phone_number
        self.username = username
        self.password = password

    @staticmethod
    def select():
        query = "SELECT * FROM foydalanuvchi ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"INSERT INTO customer(name,last_name,years_old,phone_number) VALUES('{self.name}', '{self.last_name}','{self.years_old}','{self.phone_number}')"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, date, old_date):
        if column == "id":
            query = f"UPDATE customer SET {column} = '{date}' WHERE {column} = {old_date}'"

        else:
            query = f"UPDATE customer SET {column} = '{date}' WHERE {column} = '{old_date}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column: str, name: str):
        if column == "id":
            query = f"DELETE FROM city WHERE {column} = {name}"
        else:
            query = f"DELETE FROM city WHERE {column} = '{name}'"
        return Database.connect(query, "delete")

    @staticmethod
    def personal_date(username, password):
        query = f"SELECT * FROM foydalanuvchi WHERE username = '{username}' and password = '{password}'"
        return Database.connect(query, "select")
    #@staticmethod
    #def personaml_out(username, password):
    #  query = f"DELETE FROM foydalanuvchi WHERE username='{username}' and password='{password}'"
    # Database.connect(query, "dalete")


class Product:
    def __init__(self, name, price, count, start_date, end_date, star_count, serial_number, store_id, categoty_id, ):
        self.name = name
        self.price = price
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.star_count = star_count
        self.serial_number = serial_number
        self.store_id = store_id
        self.categoty_id = categoty_id

    @staticmethod
    def select():
        query = "SELECT p.name, p.price, p.count,p.start_date,p.end_date,p.star_count,p.serial_number, s.name as Storeid, c.name as Categoryid FROM product p INNER JOIN store s ON p.store_id=s.id  INNER JOIN category c ON p.categoty_id=c.id"
        date = Product.select()
        for i in date:
            print(f"""
                Id: {i[0]}
                Name: {i[1]}
                Price: {i[2]}
                Count: {i[2]}
                Start date: {i[3]}
                End date:  {i[4]}
                Star count:  {i[5]}
                Serial number:  {i[6]}
                Store id:  {i[7]}
                Category id: {i[8]}
                """)
        return Database.connect(query, "select")
    def insert(self):
        query = (
            f"INSERT INTO product(name,price,count ,start_date,end_date,star_count, serial_number, store_id, categoty_id) VALUES ('{self.name}',{self.price},'{self.count}','{self.start_date}','{self.end_date}','{self.star_count}','{self.serial_number}','{self.store_id}','{self.categoty_id}')")
        return Database.connect(query, "insert")

    @staticmethod
    def search(name):
        query = (
            f" SELECT * FROM product WHERE name LIKE '%{name}%'")
        return Database.connect(query, "select")

    @staticmethod
    def update(column, date, old_date):
        if column == "id":
            query = f"UPDATE product SET {column} = '{date}' WHERE {column} = {old_date}'"

        else:
            query = f"UPDATE product SET {column} = '{date}' WHERE {column} = '{old_date}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM product WHERE {column} = {name}"
        else:
            query = f"DELETE FROM product WHERE {column} = '{name}'"
        return Database.connect(query, "delete")
