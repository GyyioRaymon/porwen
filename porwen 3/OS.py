import sys
print("Aug Porwen Server 2019")
print("Copyright 2019-2020")
print("please wait")
print("enter your password")
password = input()
while password != "august":
    if password == "august":
        print("welcome to Porwen")
    else:
        print("sorry, that is incorrect")
        print("enter your password")
        password = input()
while True:
    print("press q for Porwen Docs;press w for calculator;press e for mad libs;press r to quit porwen")
    choice = input()
    if choice == "q":
        print("Porwen Docs:loading")
        print("press enter to save")
        print()
        doc = input()
        print()
    if choice == "w":
            print("Porwen calculator")
            print("here is a additon only calculator")
            num1 = input("Enter a number...")
            num2 = input("Enter another number...")
            result = int(num1) + int(num2)
            print(result)
    if choice == "e":
        print("Porwen Mad Libs")
        color = input("enter a color: ")
        plural_noun = input("enter a plural noun: ")
        person = input("enter a person: ")
        print("                             ")
        print("Roses are " + color)
        print(plural_noun + " are blue")
        print("i love " + person)
    if choice == "r":
        print("please wait while porwen quits programs")
        print("you may now close this program")
        exit()

     