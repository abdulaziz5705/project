from project import product_table
from project import customer_table
from project import store_table


def admin():
    web = input("""
    
    <<<<<Welcome to Admin page you can change the information and delete>>>>>>
         
        1.Product        
        2.View customers         
        3.View store            
         >>>>>""")
    "Productda siz maxsulotni select, insert, delete, alter qismlarini ko'rishingiz mumkun"
    "Bu qismda xaridorlar ro'xatini ko'rishingiz mumkun"
    "Bu qismda xaridorlar ro'xatini ko'rishingiz mumkun"

    if web == "1":
        return product_table()
    elif web == "2":
        return customer_table()
    elif web == "3":
        return store_table()
    else:
        print("Error")
        return admin()


if __name__ == "__main__":
    admin()
