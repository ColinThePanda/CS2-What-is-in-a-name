import keyboard
import os
import time

def menu():
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
    selection = menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(selection)

if __name__ == "__main__":
    main()