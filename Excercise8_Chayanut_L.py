userName = "Ice"
passWord = "1234"
userInput = input("Username : ")
passInput = input("Password : ")
if userInput == "Ice" and passInput == "1234":
    print("Welcome", userName)
    print("""***This is Product list***  
    1.pencil >>>> 10 THB
    2.pen    >>>> 25 THB
    3.notebook >>>> 30 THB
    4.rulers >>>>10 THB 
    -1 for exit  """)
    userSelected = int(input("Choose your Product >>> "))
    pricePencil = 10
    pricePen = 25
    priceNotebook = 30
    priceRulers = 10
    if userSelected == 1:
        print("How much do you want? : ")
        count = int(input())
        totalPrice = count*pricePencil
        print("Total price = ",totalPrice,"THB","Thank you!!")
    elif userSelected ==2:
        print("How much do you want? : ")
        count = int(input())
        totalPrice = count*pricePen
        print("Total price = ", totalPrice,"THB","Thank you!!")
    elif userSelected == 3:
        print("How much do you want? : ")
        count = int(input())
        totalPrice = count * priceNotebook
        print("Total price = ", totalPrice,"THB","Thank you!!")
    elif userSelected == 4:
        print("How much do you want? : ")
        count = int(input())
        totalPrice = count * priceRulers
        print("Total price = ", totalPrice,"THB","Thank you!!")
    elif userSelected == -1:
        print("Bye, See you later !")
else:
    print("Wrong Username or Password ,please try again!!! ")

