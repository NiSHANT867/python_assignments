from Calculation import addition,subtraction,multiplication,division,exponential,floordivision

class exception1(Exception):
    def __init__(self, *args):
        super().__init__(*args)

f =open("Record.txt","+at")

a = True
while a == True:
    print("This is a menu driven progrsm")
    print("1)Addition \n2)Subraction  \n3)Multiplication \n4)Division \n5)Exponential \n6)Floordivision")
    num = int(input("Enter your choice :"))
    if num == 1:
        addition.addition()
        f.write("Addition  \n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break
    
    elif num == 2:
        subtraction.subtraction()
        f.write("Subraction\n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

    elif num == 3:
        multiplication.multiplication()
        f.write("Multiplication \n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break


    elif num == 4:
        division.division()
        f.write("Division \n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

    elif num == 5:
        exponential.exponential()
        f.write("Exponential \n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break
        
    elif num == 6:
        floordivision.floordivision()
        f.write("Floordivision \n")
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

    else :
        try:
            raise exception1("Invalid choice!")
        except exception1 as e:
            print(e.args[0])
        