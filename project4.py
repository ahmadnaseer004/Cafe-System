menu = {
    "coke": 150,
    "water": 100,
    "pepsi": 150,
    "7up": 150,
    "zinger": 450,
    "grilled chicken": 450,
    "big bang beef": 500,
    "the butcher": 500,
    "american cheese": 350,
    "swiss cheese": 350,
    "bbq small": 500,
    "bbq medium": 550,
    "bbq large": 600,
    "grill small": 500,
    "grill medium": 550,
    "grill large": 600,
    "chocolate": 200,
    "strawberry": 200,
    "vanilla": 200
}

print("\n\t********MENU********")
print("1. Drinks")
print("2. Burgers")
print("3. Pizzas")
print("4. Ice-creams")
print("5. Exit")

total_count = 0
while True:
    choice = input("Enter your choice: ")

    if choice == "1":

        print("1. Coke 150Rs \t 2. Water 100Rs \n 3. Pepsi 150Rs \t 4. 7Up 150Rs")
        Drink = input("Which drink would you like to order?\n")
        if Drink == "coke" or Drink == "water" or Drink == "pepsi" or Drink == "7up":
            total_count += menu[Drink]
            print(f"The Drink {Drink} is on the board.")
            print(f"Your total bill is {total_count}")
        else:
            print(f"The drink {Drink} isn't in our menu.")

        Drink2 = input("Would you like to order more? y/n\n")
        if Drink2 == "y":

            print("1. Coke 150Rs \t 2. Water 100Rs \n 3. Pepsi 150Rs \t 4. 7Up 150Rs")
            Drink2 = input("What you wanna like to order?\n")
            if Drink2 == "coke" or Drink2 == "water" or Drink2 == "pepsi" or Drink2 == "7up":
                total_count += menu[Drink2]
                print(f"The Drink {Drink2} is on the board.")
                print(f"Your total bill is {total_count}")
            else:
                print(f"The drink {Drink2} isn't in our menu.")

        else:
            print("Thank you for order.")
            print(f"Your total bill is {total_count}")

    elif choice == "2":

        print("\n 1. Grilled Chicken 450Rs \t 2. Zinger 450Rs \n 3. Big Bang Beef 500Rs \t 4. The Butcher 500Rs\n")
        Burger = input("Which Burger would you like to order?\n")
        if Burger == "grilled chicken" or Burger == "zinger" or Burger == "big bang beef" or Burger == "the butcher":
            total_count += menu[Burger]
            print(f"Your burger {Burger} is on board.")
            print(f"Your  bill: {total_count}Rs")
        else:
            print(f"The order {Burger} isn't in our menu.")

        Burger2 = input("Would you like to order more? y/n\n")
        if Burger2 == "y":
            print("\n 1. Grilled Chicken 450Rs \t 2. Zinger 450Rs \n 3. Big Bang Beef 500Rs \t 4. The Butcher 500Rs\n")
            Burger2 = input("What you wanna like to order?\n")
            if Burger2 == "grilled chicken" or Burger2 == "zinger" or Burger2 == "big bang beef" or Burger2 == "the butcher":
                total_count += menu[Burger2]
                print(f"Your burger {Burger2} is on board.")
                print(f"Your  bill: {total_count}Rs")
            else:
                print(f"The order {Burger2} isn't in our menu.")
        else:
            print("Thank you for order.")
            print(f"Your  bill: {total_count}Rs")

        Cheese = input(
            "Would you like to Add cheese in your order?(350Rs) y/n\n")
        if Cheese == "y":
            print("1. American Cheese \t 2. Swiss Cheese")
            Cheese = input("Which cheese do you want?\n")
            if Cheese == "american cheese" or Cheese == "swiss cheese":
                total_count += menu[Cheese]
                print(f"The toping {Cheese} is added.")
                print(f"Your  bill: {total_count}Rs")

            else:
                print("Ok! no cheese.")
                print(f"Your  bill: {total_count}Rs")

    elif choice == "3":
        print("\n 1. BBQ Pizza(small 500Rs, Medium 550Rs, Large 600Rs) \n\n 2. Grilled Pizza(small 500Rs, Medium 550Rs, Large 600Rs)")
        Pizza = input(
            "Which Pizza would you like to order? also tell its size:\n")
        if Pizza == "bbq small" or Pizza == "bbq medium" or Pizza == "bbq large" or Pizza == "grill small" or Pizza == "grill medium" or Pizza == "grill large":
            total_count += menu[Pizza]
            print(f"The Pizza {Pizza} is on the board.")
            print(f"Your bill is {total_count}")
        else:
            print("This pizza isn't in our menu.")

        Pizza2 = input("Would you like to order more? y/n\n")
        if Pizza2 == "y":
            Pizza2 = input(
                "Which Pizza would you like to order? also tell its size:\n")
            if Pizza2 == "bbq small" or Pizza2 == "bbq medium" or Pizza2 == "bbq large" or Pizza2 == "grill small" or Pizza2 == "grill medium" or Pizza2 == "grill large":
                total_count += menu[Pizza2]
                print(f"The Pizza {Pizza2} is on the board.")
                print(f"Your bill is {total_count}")
            else:
                print("This pizza isn't in our menu.")

        else:
            print("Thank you for order.")
            print(f"Your total bill is {total_count}")

    elif choice == "4":

        print("1. chocolate 200Rs \t 2. strawberry 200Rs \n 3. vanilla 200Rs")
        Cream = input("Which Ice-Cream flavour would you like to order?\n")

        if Cream == "chocolate" or Cream == "strawberry" or Cream == "vanilla":
            total_count += menu[Cream]
            print(f"The Ice-Cream {Cream} is on the board.")
            print(f"Your bill is {total_count}")

        else:
            print(f"The ice-cream {Cream} isn't in our menu.")

        Cream2 = input("Would you like to order more? y/n\n")

        if Cream2 == "y":
            print("1. chocolate 200Rs \t 2. strawberry 200Rs \n 3. vanilla 200Rs")
            Cream2 = input("What flavour do you wanna like to order?\n")
            if Cream2 == "chocolate" or Cream2 == "strawberry" or Cream2 == "vanilla":
                total_count += menu[Cream2]
                print(f"The Ice-Cream {Cream2} is on the board.")
                print(f"Your bill is {total_count}")
            else:
                print(f"The ice-cream {Cream2} isn't in our menu.")

    elif choice == "5":
        print("\n\t*********Thanks for order, Take care & Good bye.*********")
        print(f"\n\t*********Your grand total is {total_count}Rs*********")
        break

    else:
        print("worng option, select the above options.")
