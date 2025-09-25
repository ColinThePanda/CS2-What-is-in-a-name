import msvcrt
import os
from typing import Dict, Callable
from string_util import join, remove_char, upper, lower, split, counter, mix_up_letters, lowercase_letters



def reverse(name: str) -> str:
    """
    Reverses a string

    Args:
        name (str): input string

    Returns:
        str: reversed string
    """
    return join([name[i] for i in range(len(name)-1, -1, -1)])

def num_vowels(name: str) -> int:
    """
    Returns the number of vowels in a string

    Args:
        name (str): input string

    Returns:
        int: number of vowels
    """
    counts : Dict[str, int] = counter(lower(remove_char(name, " ")))
    num_vowels = sum([counts.get(vowel, 0) for vowel in ["a", "e", "i", "o", "u"]])
    return num_vowels


def consonant_frequency(name: str) -> float:
    """
    Returns the ratio of consonants to total characters

    Args:
        name (str): input string

    Returns:
        float: ratio of consonants (0-1)
    """
    vowels = num_vowels(name)
    letters = join([char for char in lower(remove_char(name, " ")) if char in lowercase_letters])
    return (len(letters) - vowels) / vowels


def split_names(name: str) -> list[str]:
    """
    Splits a string by spaces

    Args:
        name (str): input string

    Returns:
        list[str]: the sub-strings once seperated by spaces
    """
    names = split(name)
    names = list(filter(lambda name: name != "" and name != None, names))
    return names


def first_name(name: str) -> str:
    """
    Returns the first sub-string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: first sub-string
    """
    return split_names(name)[0]


def last_name(name: str) -> str:
    """
    Returns the last sub-string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: last sub-string
    """
    return split_names(name)[-1]


def middle_names(name: str) -> str | list[str]:
    """
    Returns the sub-string(s) when seperated by spaces, excluding first and last

    Args:
        name (str): input string

    Returns:
        str | list[str]: str if only one middle sub-string, or list of string if multiple
    """
    middle_names: list[str] = split_names(name)[1:-1]
    middle_names = middle_names[0] if len(middle_names) == 1 else middle_names
    return middle_names if len(middle_names) > 0 else None


def contains_hyphen(name: str) -> bool:
    """
    Returns whether a hyphen is in a string

    Args:
        name (str): input string

    Returns:
        bool: whether string contains a hyphen
    """
    return "-" in name


def lowercase(name: str) -> str:
    """
    Returns the lowercase version of a string

    Args:
        name (str): input string

    Returns:
        str: lowercase string
    """
    return lower(name)


def uppercase(name: str) -> str:
    """
    Returns the uppercase version of a string

    Args:
        name (str): input string

    Returns:
        str: uppercase string
    """
    return upper(name)


def mix_up_name(name: str) -> str:
    """
    Shuffles letters in every sub-string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: shuffled string
    """
    names = split_names(name)
    mixed_names = [mix_up_letters(str) for str in names]
    return join(mixed_names, " ")


def is_palindrome(name: str) -> bool:
    """
    Returns whether a string is a palindrome

    Args:
        name (str): input string

    Returns:
        bool: whether string is a palindrome
    """
    name = lower(remove_char(name, " "))
    return name == reverse(name)


def sort_name(name: str) -> str:
    """
    Sorts a string in alphabetical order

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    return join(sorted(name))


def initials(name: str) -> str:
    """
    Returns first character in each sub-string of a string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: first character in each sub-string of a string when seperated by spaces
    """
    names = split_names(name)
    initials = [name[0] for name in names]
    return join(upper(initials))


def contains_title(name: str) -> bool:
    """
    Returns whether a name contains common titles

    Args:
        name (str): input string

    Returns:
        bool: whether string contains title
    """
    titles = ["dr", "phd", "sir", "esq", "ms", "mrs"]
    return any(
        [title in lower(remove_char(remove_char(name, " "), ".")) for title in titles]
    )


def menu() -> int:
    """
    Runs a loop, displaying every function as an option, and then returning the number of the option selected\n
    Options include:
    1. Reverse
    2. Num of Vowels
    3. Consonant Frequency
    4. First Name
    5. Last Name
    6. Middle Name(s)
    7. Contains Hyphen
    8. Lowercase
    9. Uppercase
    10. Mix Up Letters
    11. Is Palindrome
    12. Sorted
    13. Initials
    14. Contains Title
    
    Returns:
        int: selection
    """
    selections = [
        "1. Reverse",
        "2. Num of Vowels",
        "3. Consonant Frequency",
        "4. First Name",
        "5. Last Name",
        "6. Middle Name(s)",
        "7. Contains Hyphen",
        "8. Lowercase",
        "9. Uppercase",
        "10. Mix Up Letters",
        "11. Is Palindrome",
        "12. Sorted",
        "13. Initials",
        "14. Contains Title",
    ]

    selection = 1
    running = True

    while running:
        os.system("cls" if os.name == "nt" else "clear")
        for i, choice in enumerate(selections):
            print(f"\033[42m{choice}\033[0m" if selection == i + 1 else choice)

        action_made = False
        while not action_made:
            while not msvcrt.kbhit():
                pass

            key_byte = msvcrt.getch()

            if key_byte == b"\xe0":  # arrow key
                arrow_key = msvcrt.getch()
                match arrow_key:
                    case b"H":  # up
                        selection -= 1
                        action_made = True
                    case b"P":  # down
                        selection += 1
                        action_made = True
            elif key_byte == b" " or key_byte == b"\r": # space or enter
                action_made = True
                running = False

        if selection < 1:
            selection = len(selections)
        if selection > len(selections):
            selection = 1

    return selection


def main():
    selection: int = menu()
    os.system("cls" if os.name == "nt" else "clear")
    name: str = input("What is your name? ")

    function_key: Dict[Callable] = {
        1: reverse,
        2: num_vowels,
        3: consonant_frequency,
        4: first_name,
        5: last_name,
        6: middle_names,
        7: contains_hyphen,
        8: lowercase,
        9: uppercase,
        10: mix_up_name,
        11: is_palindrome,
        12: sort_name,
        13: initials,
        14: contains_title,
    }

    function = function_key.get(selection)
    function_call = lambda name: function(name)
    result = function_call(name)
    print(result)


if __name__ == "__main__":
    main()
