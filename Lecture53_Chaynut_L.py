def vatCal(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
inputPrice =  int(input("Enter price : "))
print(vatCal(inputPrice))