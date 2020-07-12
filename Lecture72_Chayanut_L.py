menuList = []
def showBill():
    print("Food list".center(15,"-"))
    for i in range(len(menuList)):
        print(menuList[i][0],"=",menuList[i][1])
    totalPrice()

def totalPrice():
    result = 0
    for i in range(len(menuList)):
            result = result+menuList[i][1]
    print("Total Price =",result)

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else: menuPrice = int(input("Price : "))
  menuList.append([menuName,menuPrice])

showBill()