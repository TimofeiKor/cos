import os
import apps.calc

def note():
    os.system('cls')
    filename = "notes.txt"

    content = ""
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")

    if content:
        print(content)
    else:
        print("File is empty")

    new_text = input("Enter new text: ").strip()
    with open(filename, "a") as file:
        file.write(new_text + "\n")



def menu():
    os.system('cls')
    calc = "calc"
    note_t = "note"
    
    print("COS. alpha 0.0.0.4 (build 57)")
    print("======== MENU ========")
    print(calc)
    print(note_t)
    print("======================")
    answ = input("input a program: ")
    if answ == calc:
        apps.calc.plus()
        answ = int(input("Input '0' to close program... "))
        if answ == 0:
            menu()
    elif answ == note_t:
        note()
        answ = int(input("Input '0' to close program... "))
        if answ == 0:
            menu()

menu()