from classes import Country
from classes import City
from classes import Address
from classes import Category
from classes import Store
from classes import Customer
from classes import Product


def product_table():
    product = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>>>""")
    if product == "1":
        Product.select()
        back = input("""
            0.Back   
             >>>""")
        if back == "0":
            return product_table()
        else:
            return product_table()



    elif product == "2":
        name = input("Name: ")
        price = input("Price: ")
        count = input("Count: ")
        start_date = input("start_date: ")
        end_date = input("end_date: ")
        star_count = input("star_count: ")
        serial_number = input("serial_number: ")
        store_id = input("store_id: ")
        category_id = input("category_id: ")
        customer = Product(name, price, count, start_date, end_date, star_count, serial_number, store_id, category_id)
        print(customer.insert())
        return product_table()
    elif product == "3":
        column = input("Column name: ")
        date = input("New_name: ")
        old = input("Old_name: ")
        print(Product.update(column, date, old))
        return product_table()

    elif product == "4":
        column = input("Column name: ")
        name = input("Name: ")
        print(Product.delete(column, name))
        return product_table()


    elif product == "0":
        return product_table()

    else:
        print("Error")
        return product_table()


def customer_table():
    customer = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>>""")
    if customer == "1":
        Customer.select()
        back = input("""
        0.Back
        >>>""")
        if back == "0":
            return customer_table()
        else:
            return customer_table()
    elif customer == "2":
        name = input("Name: ")
        last_name = input("Last_name: ")
        year = input("Years_old: ")
        phone_number = input("Phone_number: ")
        username = input("Username: ")
        password = input("Password: ")
        password1 = input("Passwordni qaytadan kiriting: ")
        customer = Customer(name, last_name, year, phone_number, username, password)
        print(customer.insert())
        return customer_table()
    elif customer == "3":
        column = input("Column name: ")
        date = input("New_name: ")
        old_date = input("Old_name: ")
        print(Customer.update(column, date, old_date))
        return customer_table()
    elif customer == "4":
        column = input("Column name: ")
        name = input("Name: ")
        print(Customer.delete(column, name))
        return customer_table()
    elif customer == "0":
        return main()
    else:
        print("Error")
        return customer_table()


def store_table():
    store = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>""")
    if store == "1":
        Store.select()
        back = input("""
            0.Back
        >>>""")
        if back == "0":
            return store_table()
        else:
            return store_table()

    if store == "2":
        name = input("Name: ")
        star = input("Star_count: ")
        open = input("open_date: ")
        address = input("address_id: ")
        store = Store(name, star, open, address)
        print(store.insert())
        return store_table()
    if store == "3":
        column = input("Column name: ")
        date = input("New_name: ")
        old_date = input("Old_name: ")
        print(Store.update(column, date, old_date))
        return store_table()
    if store == "4":
        column = input("Column name: ")
        name = input("Name: ")
        print(Store.delete(column, name))
        return store_table()

    elif store == "0":
        return main()
    else:
        print("Error")
        return store_table()


def category_table():
    category = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>""")
    if category == "1":
        Category.select()
        back = input("""
         0.Back
         >>>""")
        if back == "0":
            return category_table()
        else:
            return category_table()

    elif category == "2":
        name = input("Name: ")
        category = Category(name)
        print(category.insert())
        return category_table()
    elif category == "3":
        column = input("Column name: ")
        date = input("Name: ")
        old_date = input("Old name row: ")
        print(Category.update(column, date, old_date))
        return category_table()
    elif category == "4":
        column = input("Column name: ")
        name = input("Name: ")
        print(Category.delete(column, name))
        return category_table()

    elif category == "0":
        return main()
    else:
        print("Error")
        return category_table()


def address_table():
    a = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>""")
    if a == "1":
        Address.select()
        back = input("""
                        0.Back
                    >>>""")
        if back == "0":
            return address_table()
        else:
            return address_table()
    elif a == "2":
        name = input("Name: ")
        city_id = input("City_id: ")
        address = Address(name, city_id)
        print(address.insert())
        return address_table()
    if a == "3":
        column = input("Column name: ")
        date = input("New_name: ")
        old_name = input("Old_name: ")
        print(Address.update(column, date, old_name))
        return address_table()
    elif a == "4":
        column = input("Column name: ")
        name = input("Name delete row: ")
        print(Address.delete(column, name))
        return address_table()
    elif a == "0":
        return main()

    else:
        print("Error")
        return address_table()


@staticmethod
def city_table():
    choose1 = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>> """)
    if choose1 == "1":
        City.select()
        back = input("""
                0.Back
            >>>""")
        if back == "0":
            return city_table()
        else:
            print("Error")
            return city_table()

    elif choose1 == "2":
        name = input("Name: ")
        country_id = input("country_id: ")
        city = City(name, country_id)
        print(city.insert(name, country_id))
        return city_table()
    elif choose1 == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old name: ")
        print(City.update(column, new_name, old_name))
        return city_table()
    elif choose1 == "4":
        column = input("Column name: ")
        name = input("O'chirmoqchi bo'lgan rowning  nomini kiriting: ")
        print(City.delete(column, name))
        return city_table()
    elif choose1 == "0":
        return main()
    else:
        print("Error")
        return city_table()


@staticmethod
def country_table():
    choose = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        
        >>>>""")
    if choose == "1":
        Country.select()
        back = input("""
        0.Back
    >>>""")
        if back == "0":
            return country_table()
        else:
            print("Error")
            return country_table()
    elif choose == "2":
        name = input("Name: ")
        country = Country(name)
        print(country.insert())
        return country_table()

    elif choose == "3":
        column = input("Column name: ")
        new_name = input("new_date: ")
        old_name = input("old_date: ")
        print(Country.update(column, new_name, old_name))
        return country_table()


    elif choose == "4":
        column = input("Column name: ")
        name = input("Name date: ")
        print(Country.delete(column, name))
        return country_table()


    elif choose == "0":
        return main()
    else:
        print("Error")
        return country_table()


def main():
    tables = input("""
    
   
    
        1.Country
        2.City
        3.Address
        4.Category
        5.Store
        6.Customer
        7.Product
        >>>>>"""
                   )

    if tables == "1":
        return country_table()
    elif tables == "2":
        return city_table()
    elif tables == "3":
        return address_table()
    elif tables == "4":
        return category_table()
    elif tables == "5":
        return store_table()
    elif tables == "6":
        return customer_table()
    elif tables == "7":
        return product_table()
    else:

        #else:
        print("Error")
        return main()


if __name__ == "__main__":
    main()
