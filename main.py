import os
import datetime
import random

calc_t = "calc"
note_t = "note"
cmdcore = "core"
timecmd = "time"
randncmd = "rndnms"

def time():
    clear()
    now = datetime.datetime.now()
    print(now)
    answ = int(input("Input '0' to close program... "))
    if answ == 0:
        menu()

def randNum():
    clear()
    minR = int(input("input min num: "))
    maxR = int(input("input max num: "))
    randN = random.randint(minR, maxR)
    answer = int(input("input your number: "))
    while answer != randN:
        answer = int(input("input your number: "))
        if answer == randN:
            print("Right answer!")
            answ = int(input("Input '0' to close program... "))
            if answ == 0:
                menu()
            elif answer != randN:
                answer = int(input("input your number: "))


def info():
    print("COS. alpha 0.0.0.5.4 (build 113)")

def info_core():
    print("COS Core. alpha 0.0.0.1.3 (build 30)\nMade by: @TimofeiKor (github.com/TimofeiKor)")

def clear():
    os.system('cls')

def core():
    clear()
    info_core()
    cmd = input("cos/core/> ")
    if cmd == "0":
        menu()
    elif cmd == calc_t:
        question()
    elif cmd == note_t:
        note()
    elif cmd == timecmd:
        time()
    elif cmd == randncmd:
        randNum()



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
    print(timecmd)
    print(randncmd)
    print("======================")
    answ = input("input a program: ")
    if answ == calc_t:
        question()
    elif answ == note_t:
        note()
    elif answ == cmdcore:
        core()
    elif answ == timecmd:
        time()
    elif answ == randncmd:
        randNum()


menu()