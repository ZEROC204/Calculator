print("CALCULATOR")
def Options():
    print('''[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Exit''')

    Opt = input("Choose an option ( Enter a number ):  ")
    if Opt == "1":
        print("ADDITION")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        sum = float(num1) + float(num2)
        print("Sum: ", sum)
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")

    elif Opt == "2":
        print("SUBTRACTION")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        diff = float(num1) - float(num2)
        print("Difference: ", diff)
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")



    elif Opt == "3":
        print("MULTIPLICATION")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        pro = float(num1) * float(num2)
        print("Product: ", pro)
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")




    elif Opt == "4":
        print("DIVISION")
        num1 = input("Enter the divisor: ")
        num2 = input("Enter the dividend: ")
        div = float(num1) / float(num2)
        div2 = float(num1) % float(num2)
        print("Quotient: ", div)
        print("Remainder: ", div2)
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")

    elif Opt == "5":
        print("Quiting process.")
        exit(0)

    else:
        print("PLease enter any number from 1-5.")
        Options()


Options()

