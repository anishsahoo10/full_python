print("1.India , 2, japan ,3.korea")
a= int(input("enter number : "))

match a:
    case 1:
        print("selected country=India")
    case 2:
        print("selected country=Japan")
    case 3:
        print("selected country=Korea")
    case _:
        print("end")