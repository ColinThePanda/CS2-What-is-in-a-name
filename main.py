import keyboard
import os
from typing import Dict, Callable

def reverse(name : str) -> str:
    pass

def num_vowels(name : str) -> int:
    pass

def consonant_frequency(name : str):
    pass

def first_name(name : str) -> str:
    pass

def last_name(name : str) -> str:
    pass

def middle_names(name : str) -> str | list[str]:
    pass

def contains_hyphen(name : str) -> bool:
    pass

def lowercase(name : str) -> str:
    pass

def uppercase(name : str) -> str:
    pass

def num_vowels(name : str) -> int:
    pass

def mix_up_letters(name : str) -> str:
    pass

def is_palindrome(name : str) -> bool:
    pass

def sorted(name : str) -> str:
    pass

def initials(name : str) -> str:
    pass

def contains_title(name : str) -> bool:
    pass


def menu() -> int:
    selections = ["1. Reverse",
     "2. Num of Vowels",
     "3. Consonant Frequency",
     "4. First Name",
     "5. Last Name",
     "6. Middle Name(s)",
     "7. Contains Hyphen",
     "8. Lowercase",
     "9. Upercase",
     "10. Mix Up Letters",
     "11. Is Palindrome",
     "12. Sorted",
     "13. Initials",
     "14. Contains Title"]
    
    selection = 1
    running = True
    
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, choice in enumerate(selections):
            print(f"\033[32m{choice}\033[0m" if selection == i+1 else choice)
        key = keyboard.read_key()

        match key:
            case "up":
                selection -= 1
                while keyboard.is_pressed("up"): pass
            case "down":
                selection += 1
                while keyboard.is_pressed("down"): pass
            case "space":
                break
        
        if selection < 1:
            selection = len(selections)
        if selection > len(selections):
            selection = 1
    
    return selection


def main():
    selection : int = menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    name : str = input("What is your name?")
    
    function_key : Dict[Callable] = {
        1 : reverse,
        2 : num_vowels,
        3 : consonant_frequency,
        4 : first_name,
        5 : last_name,
        6 : middle_names,
        7 : contains_hyphen,
        8 : lowercase,
        9 : uppercase,
        10 : mix_up_letters,
        11 : is_palindrome,
        12 : sorted,
        13 : initials,
        14 : contains_title
    }
    
    function = function_key.get(selection)
    function_call = lambda name : function(name)
    function_call(name)
    
    
    

if __name__ == "__main__":
    main()