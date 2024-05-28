from asosiy import Check
from website import website

def login_page(username=None):
    print("             <<<<<<Login Page>>>>   ")
    user = input("Username: ")
    password = input("Password: ")
    if Check.login_check(user, password):
        return website(username, password)
    else:
        print("<<<Login or password Error Please replay >>>")
        return login_page()




