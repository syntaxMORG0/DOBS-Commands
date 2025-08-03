import os
import json
from colorama import init, Fore, Style

#Made by syntaxMORG0
#please star my github repo

init(autoreset=True)

DATA_FILE = "dobs_data.json"

def on_start():
    os.system("clear")
    print(Fore.CYAN + Style.BRIGHT + "𝑫𝑶𝑩𝑺")
    print(Fore.YELLOW + "2025 made by syntaxMORG0 on github\n")
    print(Fore.MAGENTA + Style.BRIGHT + "Type HELP for commands.\n" + Style.RESET_ALL)
    print(Fore.WHITE + Style.DIM + "Powered by 𝑫𝑶𝑩𝑺\n" + Style.RESET_ALL)

def handle_print(line_number):
    user_input = input(Fore.GREEN + f"{line_number} PRINT> " + Style.RESET_ALL)
    print(Fore.GREEN + f"{line_number}> {user_input}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_help():
    print(Fore.MAGENTA + "Available commands:")
    print("  PRINT    - Print a string")
    print("  HELP     - Show this help message")
    print("  EXIT     - Exit the program")
    print("  ADD      - Add two numbers")
    print("  MUL      - Multiply two numbers")
    print("  SUB      - Subtract two numbers")
    print("  DIV      - Divide two numbers")
    print("  POW      - Power of two numbers")
    print("  MOD      - Modulo of two numbers")
    print("  FACT     - Factorial of a number")
    print("  REVERSE  - Reverse a string")
    print("  UPPER    - Convert string to uppercase")
    print("  LOWER    - Convert string to lowercase")
    print("  CLEAR    - Clear the screen")
    print("  ABOUT    - Show about info")
    print("  OPEN     - Open a URL in your browser")
    print("  IF       - Evaluate a condition")
    print("  SAVE     - Save data to file")
    print("  LOAD     - Load data from file")
    print("  SET      - Set a key-value pair in data")
    print("  DEL      - Delete a key from data")
    print("  KEYS     - List all keys in data")
    print("  SHOW     - Show value for a key")
    print("  LEN      - Show number of keys in data")
    print("  ECHO     - Echo a message")
    print("  UPDATE   - Update value for a key")
    print("  EXPORT   - Export data to a file")
    print("  IMPORT   - Import data from a file")
    print("  COPY     - Copy a key to a new key")
    print("  RENAME   - Rename a key")

def handle_unknown(command):
    print(Fore.RED + f"ERROR: Unknown command '{command}'")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_add(line_number):
    try:
        a = float(input(f"{line_number} ADD> First number: "))
        b = float(input(f"{line_number} ADD> Second number: "))
        print(Fore.BLUE + f"{line_number}> Result: {a + b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_sub(line_number):
    try:
        a = float(input(f"{line_number} SUB> First number: "))
        b = float(input(f"{line_number} SUB> Second number: "))
        print(Fore.BLUE + f"{line_number}> Result: {a - b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_mul(line_number):
    try:
        a = float(input(f"{line_number} MUL> First number: "))
        b = float(input(f"{line_number} MUL> Second number: "))
        print(Fore.BLUE + f"{line_number}> Result: {a * b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_div(line_number):
    try:
        a = float(input(f"{line_number} DIV> Numerator: "))
        b = float(input(f"{line_number} DIV> Denominator: "))
        if b == 0:
            print(Fore.RED + f"{line_number}> ERROR: Division by zero.")
        else:
            print(Fore.BLUE + f"{line_number}> Result: {a / b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_pow(line_number):
    try:
        a = float(input(f"{line_number} POW> Base: "))
        b = float(input(f"{line_number} POW> Exponent: "))
        print(Fore.BLUE + f"{line_number}> Result: {a ** b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_mod(line_number):
    try:
        a = float(input(f"{line_number} MOD> Dividend: "))
        b = float(input(f"{line_number} MOD> Divisor: "))
        if b == 0:
            print(Fore.RED + f"{line_number}> ERROR: Modulo by zero.")
        else:
            print(Fore.BLUE + f"{line_number}> Result: {a % b}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_fact(line_number):
    try:
        n = int(input(f"{line_number} FACT> Number: "))
        if n < 0:
            print(Fore.RED + f"{line_number}> ERROR: Negative number.")
        else:
            result = 1
            for i in range(2, n+1):
                result *= i
            print(Fore.BLUE + f"{line_number}> Result: {result}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + f"{line_number}> ERROR: Invalid number.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_reverse(line_number):
    s = input(f"{line_number} REVERSE> String: ")
    print(Fore.BLUE + f"{line_number}> {s[::-1]}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_upper(line_number):
    s = input(f"{line_number} UPPER> String: ")
    print(Fore.BLUE + f"{line_number}> {s.upper()}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_lower(line_number):
    s = input(f"{line_number} LOWER> String: ")
    print(Fore.BLUE + f"{line_number}> {s.lower()}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_clear():
    os.system("clear")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_about():
    print(Fore.CYAN + "𝑫𝑶𝑩𝑺 - A simple command interpreter.")
    print(Fore.YELLOW + "2025 made by syntaxMORG0 on github")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_open(line_number):
    url = input(f"{line_number} OPEN> Enter URL: ")
    if url:
        os.system(f'$BROWSER "{url}"')
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"{line_number}> ERROR: No URL provided.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_if(line_number):
    condition = input(f"{line_number} IF> Enter a condition (e.g. 5 > 3): ")
    try:
        allowed_names = {"__builtins__": None}
        result = eval(condition, allowed_names, {})
        if result:
            print(Fore.BLUE + f"{line_number}> Condition is TRUE")
        else:
            print(Fore.YELLOW + f"{line_number}> Condition is FALSE")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
    except Exception:
        print(Fore.RED + f"{line_number}> ERROR: Invalid condition.")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_save(line_number, data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        print(Fore.BLUE + f"{line_number}> Data saved to {DATA_FILE}")
    except Exception as e:
        print(Fore.RED + f"{line_number}> ERROR: Could not save data. {e}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_load(line_number):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        print(Fore.BLUE + f"{line_number}> Data loaded: {data}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
        return data
    except Exception as e:
        print(Fore.RED + f"{line_number}> ERROR: Could not load data. {e}")
        print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
        return {}

def handle_set(line_number, data):
    key = input(f"{line_number} SET> Key: ")
    value = input(f"{line_number} SET> Value: ")
    data[key] = value
    print(Fore.BLUE + f"{line_number}> Data set: {key} = {value}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_del(line_number, data):
    key = input(f"{line_number} DEL> Key: ")
    if key in data:
        del data[key]
        print(Fore.BLUE + f"{line_number}> Data deleted: {key}")
    else:
        print(Fore.RED + f"{line_number}> ERROR: Key not found.")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_keys(line_number, data):
    print(Fore.BLUE + f"{line_number}> Keys: {list(data.keys())}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_show(line_number, data):
    key = input(f"{line_number} SHOW> Key: ")
    if key in data:
        print(Fore.BLUE + f"{line_number}> {key} = {data[key]}")
    else:
        print(Fore.RED + f"{line_number}> ERROR: Key not found.")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_len(line_number, data):
    print(Fore.BLUE + f"{line_number}> Data length: {len(data)}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_echo(line_number):
    msg = input(f"{line_number} ECHO> Message: ")
    print(Fore.BLUE + f"{line_number}> {msg}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_update(line_number, data):
    key = input(f"{line_number} UPDATE> Key: ")
    if key in data:
        value = input(f"{line_number} UPDATE> New Value: ")
        data[key] = value
        print(Fore.BLUE + f"{line_number}> Data updated: {key} = {value}")
    else:
        print(Fore.RED + f"{line_number}> ERROR: Key not found.")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_export(line_number, data):
    filename = input(f"{line_number} EXPORT> Filename: ")
    try:
        with open(filename, "w") as f:
            json.dump(data, f)
        print(Fore.BLUE + f"{line_number}> Data exported to {filename}")
    except Exception as e:
        print(Fore.RED + f"{line_number}> ERROR: Could not export data. {e}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_import(line_number, data):
    filename = input(f"{line_number} IMPORT> Filename: ")
    try:
        with open(filename, "r") as f:
            imported = json.load(f)
        data.update(imported)
        print(Fore.BLUE + f"{line_number}> Data imported from {filename}")
    except Exception as e:
        print(Fore.RED + f"{line_number}> ERROR: Could not import data. {e}")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_copy(line_number, data):
    key = input(f"{line_number} COPY> Key: ")
    new_key = input(f"{line_number} COPY> New Key: ")
    if key in data:
        data[new_key] = data[key]
        print(Fore.BLUE + f"{line_number}> {key} copied to {new_key}")
    else:
        print(Fore.RED + f"{line_number}> ERROR: Key not found.")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def handle_rename(line_number, data):
    key = input(f"{line_number} RENAME> Key: ")
    new_key = input(f"{line_number} RENAME> New Key: ")
    if key in data:
        data[new_key] = data.pop(key)
        print(Fore.BLUE + f"{line_number}> {key} renamed to {new_key}")
    else:
        print(Fore.RED + f"{line_number}> ERROR: Key not found.")
    print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)

def looped():
    line_number = 1
    data = {}
    while True:
        key_code = input(Fore.WHITE + Style.BRIGHT + f"{line_number}> " + Style.RESET_ALL).strip().upper()
        if key_code == "PRINT":
            handle_print(line_number)
        elif key_code == "HELP":
            handle_help()
        elif key_code == "EXIT":
            print(Fore.YELLOW + "Exiting...")
            print(Fore.WHITE + Style.DIM + "𝑫𝑶𝑩𝑺" + Style.RESET_ALL)
            break
        elif key_code == "ADD":
            handle_add(line_number)
        elif key_code == "SUB":
            handle_sub(line_number)
        elif key_code == "MUL":
            handle_mul(line_number)
        elif key_code == "DIV":
            handle_div(line_number)
        elif key_code == "POW":
            handle_pow(line_number)
        elif key_code == "MOD":
            handle_mod(line_number)
        elif key_code == "FACT":
            handle_fact(line_number)
        elif key_code == "REVERSE":
            handle_reverse(line_number)
        elif key_code == "UPPER":
            handle_upper(line_number)
        elif key_code == "LOWER":
            handle_lower(line_number)
        elif key_code == "CLEAR":
            handle_clear()
        elif key_code == "ABOUT":
            handle_about()
        elif key_code == "OPEN":
            handle_open(line_number)
        elif key_code == "IF":
            handle_if(line_number)
        elif key_code == "SAVE":
            handle_save(line_number, data)
        elif key_code == "LOAD":
            data = handle_load(line_number)
        elif key_code == "SET":
            handle_set(line_number, data)
        elif key_code == "DEL":
            handle_del(line_number, data)
        elif key_code == "KEYS":
            handle_keys(line_number, data)
        elif key_code == "SHOW":
            handle_show(line_number, data)
        elif key_code == "LEN":
            handle_len(line_number, data)
        elif key_code == "ECHO":
            handle_echo(line_number)
        elif key_code == "UPDATE":
            handle_update(line_number, data)
        elif key_code == "EXPORT":
            handle_export(line_number, data)
        elif key_code == "IMPORT":
            handle_import(line_number, data)
        elif key_code == "COPY":
            handle_copy(line_number, data)
        elif key_code == "RENAME":
            handle_rename(line_number, data)
        else:
            handle_unknown(key_code)
        line_number += 1

# Example usage:
# on_start()
# looped()
