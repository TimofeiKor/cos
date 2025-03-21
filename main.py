import os
import apps.calc

def menu():
    os.system('cls')
    calc = "calc"
    
    print("COS. alpha 0.0.0.3 (build 35)")
    print("======== MENU ========")
    print(calc)
    print("======================")
    answ = input("input a program: ")
    if answ == calc:
        apps.calc.plus()
        answ = int(input("Input '0' to close program... "))
        if answ == 0:
            menu()

menu()