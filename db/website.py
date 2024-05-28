from project import Category
from classes import Customer
from classes import Product


def website(username, password):
    web = input("""
        <<<<Welcome to our website  you can choose section >>>>
                    1.Shop
                    2.Search
                    3.Account
                    >>>>>""")
    if web == "1":
        return shop(username, password)
    elif web == "2":
        name = input("Enter your name: ")
        data = Product.search(name)
        for i in data:
            print(f"""
                        Id: {i[0]}
                        Name: {i[1]}
                        Price: {i[2]}
                        Count: {i[3]}
                        Start date: {i[4]}
                        End date:  {i[5]}
                        Star count:  {i[6]}
                        Serial number:  {i[7]}
                        Store id:  {i[8]}
                        Category id: {i[9]}
                        """)

        return Product.search(name)

    elif web == "3":
        return account(username, password)

    else:
        print("Error")
        return website(username, password)


def shop(username, password):
    service = input("""
        1.Product
        2.Category
        0.Back
         >>>>""")
    if service == "1":
        Product.select()
        back = input("""
               0.Back
               >>>""")
        if back == "0":
            return shop(username, password)
        else:
            return service
    elif service == "2":
        Category.select()
        back = input("""
                      0.Back
                      >>>""")
        if back == "0":
            return shop(username, password)
        return service
    elif service == "0":
        return website(username, password)
    else:
        print("Error")
        return shop(username, password)


def account(username, password):
    service = input("""
        1.My Personal Data
        2.Log out
        >>>>>""")
    if service == "1":
        return personal_date(username, password)
    elif service == "2":
        return
    else:
        return account(username, password)


def personal_date(username, password):
    date = Customer.personal_date(username, password)
    print(f"""
        First name: {date[0][1]}
    """)


#def log_out(username, password):
# Customer.personaml_out(username, password)
# print("Siz saytdan chiqdingiz ")
