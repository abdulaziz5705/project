from login import login_page
from enterregester import regester_page


def enter():
    log = input(""" 
        <<<<Welcome our online shop>>>
        
                1.Login
                2.Register
                >>>""")
    if log == "1":
        return login_page()
    elif log == "2":
        return regester_page()
    else:
        print("Error")
        return enter()


if __name__ == "__main__":
    enter()
