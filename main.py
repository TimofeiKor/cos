import os

calc_t = "calc"
note_t = "note"
cmdcore = "core"

def info():
    print("COS. alpha 0.0.0.5.3 (build 107)")

def info_core():
    print("COS Core. alpha 0.0.0.1.2 (build 23)")

def clear():
    os.system('cls')

def core():
    clear()
    info_core()
    cmd = input("cos/core: ")
    if cmd == "info":
        info_core()
        core()
    elif cmd == "clear":
        clear()
        core()
    elif cmd == "0":
        menu()
    elif cmd == calc_t:
        question()
    elif cmd == note_t:
        note()



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
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()

def minus():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x - y
    print("Result: ", res)
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()

def multiply():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x * y
    print("Result: ", res)
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()

def divide():
    clear()
    x = int(input("input num1: "))
    y = int(input("input num2: "))
    res = x / y
    print("Result: ", res)
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()


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
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()



def menu():
    clear()
    
    info()
    print("======== MENU ========")
    print(calc_t)
    print(note_t)
    print(cmdcore)
    print("======================")
    answ = input("input a program: ")
    if answ == calc_t:
        question()
    elif answ == note_t:
        note()
    elif answ == cmdcore:
        core()


menu()