menuList = []
priceList = []
def showBill():
    print("Food list".center(15,"-"))
    for i in range(len(menuList)):
        print(menuList[i],"=",priceList[i])
    totalPrice()

def totalPrice():
    result = 0
    for i in priceList:
        result = result+i
    print("Total Price =",result)

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else: menuPrice = int(input("Price : "))
  menuList.append(menuName)
  priceList.append(menuPrice)

showBill()