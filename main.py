import os


def clear():
    os.system('cls')


def question():
    clear()
    answ11 = input("input a math char: ")
    if answ11 == "+":
        plus()
    elif answ11 == "-":
        minus()
    elif answ11 == "*":
        multiply()
    elif answ11 == "/":
        divide()

def plus():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x + y
    print("Result: ", res)

def minus():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x - y
    print("Result: ", res)

def multiply():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x * y
    print("Result: ", res)

def divide():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x / y
    print("Result: ", res)


def note():
    clear()
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
    clear()
    calc_t = "calc"
    note_t = "note"
    
    print("COS. alpha 0.0.0.4.5 (build 83)")
    print("======== MENU ========")
    print(calc_t)
    print(note_t)
    print("======================")
    answ = input("input a program: ")
    if answ == calc_t:
        question()
        answ = int(input("Input '0' to close program... "))
        if answ == 0:
            menu()
    elif answ == note_t:
        note()
        answ = int(input("Input '0' to close program... "))
        if answ == 0:
            menu()

menu()