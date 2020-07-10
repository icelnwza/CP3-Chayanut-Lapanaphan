def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while usernameInput != "admin" or passwordInput != "1234":
        return  login()
    else: showMenu()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    if menuSelect() ==1:
        price = int(input("What price ? :"))
        print(vatCalculator(price))
    else:
      priceCalculator()

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total = price1+price2
    total = total+(vatCalculator(price1 + price2))
    return print(total)

login()
