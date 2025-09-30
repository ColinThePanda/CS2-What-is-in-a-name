"""
What is in a Name

Performs a choice of 13 different functions on someone's name.

Colin Politi

Bonus:
1. Menu as a fullscreen terminal app with colored text using ansi escape codes.
2. Interaction with keyboard using msvcrt.

Log:

v1.1 - 9/30/25 - CP
v1.0 - 9/29/25 - CP
"""

import msvcrt
import os
import sys
from typing import Dict, Callable
from string_util import (
    join,
    remove_char,
    upper,
    lower,
    split,
    counter,
    mix_up_letters,
    lowercase_letters,
)

titles = [
    "mr",
    "mrs",
    "ms",
    "miss",
    "dr",
    "prof",
    "rev",
    "fr",
    "sir",
    "madam",
    "lord",
    "lady",
    "hon",
    "judge",
    "pres",
    "gov",
    "mayor",
    "chancellor",
    "principal",
    "dean",
    "phd",
    "esq",
    "prof",
    "sr",
    "jr",
    "i",
    "ii",
    "iii",
    "ix",
    "v",
    "vi",
    "vii",
    "viii",
    "ix",
    "x",
    "xi",
    "xii",
    "xiii",
    "xiv",
    "xv",
    "xvi",
    "xvii",
    "xviii",
    "xix",
    "xx",
]


def remove_titles(name: str) -> str:
    names = split_names(name)
    no_titles = list(filter(lambda x: remove_char(remove_char(lower(x), "."), " ") not in titles, names))
    return join(no_titles, " ")


def reverse(name: str) -> str:
    """
    Reverses a string

    Args:
        name (str): input string

    Returns:
        str: reversed string
    """
    return join(
        [name[i] for i in range(len(name) - 1, -1, -1)]
    )  # starts at last char, stops at first char, goes back by one each time


def num_vowels(name: str) -> int:
    """
    Returns the number of vowels in a string

    Args:
        name (str): input string

    Returns:
        int: number of vowels
    """
    counts: Dict[str, int] = counter(
        lower(remove_char(name, " "))
    )  # number of each char in str
    num_vowels = sum(
        [counts.get(vowel, 0) for vowel in ["a", "e", "i", "o", "u"]]
    )  # number of the chars that are vowels
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
    letters = join(
        [
            char for char in lower(remove_char(name, " ")) if char in lowercase_letters
        ]  # gets total letters
    )
    return (len(letters) - vowels) / len(letters)  # consonants / total_letters


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
    return split_names(remove_titles(name))[0]


def last_name(name: str) -> str:
    """
    Returns the last sub-string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: last sub-string
    """
    return split_names(remove_titles(name))[-1]


def middle_names(name: str) -> str | list[str]:
    """
    Returns the sub-string(s) when seperated by spaces, excluding first and last

    Args:
        name (str): input string

    Returns:
        str | list[str]: str if only one middle sub-string, or list of string if multiple
    """
    no_titles = remove_titles(name)
    middle_names = split_names(no_titles)[1:-1]
    if len(middle_names) == 1:
        return middle_names[0]
    elif len(middle_names) == 0:
        return ""
    else:
        return middle_names


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
        name (str): input string

    Returns:
        str: sorted name
    """
    return join(
        sorted(join(list(filter(lambda x: lower(x) in lowercase_letters, name))))
    )


def initials(name: str) -> str:
    """
    Returns first character in each sub-string of a string when seperated by spaces

    Args:
        name (str): input string

    Returns:
        str: first character in each sub-string of a string when seperated by spaces
    """
    names = split_names(remove_titles(name))
    initials = [name[0] for name in names]  # first letter of each part of name
    return upper(join(initials))


def contains_title(name: str) -> bool:
    """
    Returns whether a name contains common titles

    Args:
        name (str): input string

    Returns:
        bool: whether string contains title
    """

    # Title before name
    pre_title = lower(
        remove_char(remove_char(split_names(name)[0], " "), ".")
    )  # gets first part of name lowercase without spaces or periods

    post_title = lower(
        remove_char(remove_char(split_names(name)[-1], " "), ".")
    )  # gets last part of name lowercase without spaces or periods
    return pre_title in titles or post_title in titles


def menu() -> tuple[int, str]:
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

    def ansi(ansi: str):
        """Helper function for using ansi escape codes"""
        sys.stdout.write(ansi)
        sys.stdout.flush()

    selections = [
        "1.  Reverse",
        "2.  Num of Vowels",
        "3.  Consonant Frequency",
        "4.  First Name",
        "5.  Last Name",
        "6.  Middle Name(s)",
        "7.  Contains Hyphen",
        "8.  Lowercase",
        "9.  Uppercase",
        "10. Mix Up Letters",
        "11. Is Palindrome",
        "12. Sorted",
        "13. Initials",
        "14. Contains Title",
    ]

    selection = 1
    running = True

    ansi("\033[?1049h")  # goes to different screen
    ansi("\033[?25l")  # hides cursor

    while running:
        os.system(
            "cls" if os.name == "nt" else "clear"
        )  # clears screen (cross platform)
        for i, choice in enumerate(selections):
            if selection == i + 1:
                print(f"\033[1;32m{choice}\033[0m")  # bold and green if selected
            else:
                print(choice)

        action_made = False
        while not action_made:
            while not msvcrt.kbhit():  # wait until pressing key
                pass

            key_byte = msvcrt.getch()  # get what key it is

            if key_byte == b"\xe0":  # arrow key
                arrow_key = msvcrt.getch()  # get which arrow key it is
                match arrow_key:
                    case b"H":  # up
                        selection -= 1
                        action_made = True
                    case b"P":  # down
                        selection += 1
                        action_made = True
            elif key_byte == b" " or key_byte == b"\r":  # space or enter
                action_made = True
                running = False

        if selection < 1:
            selection = len(selections)  # loop if press up on first selection
        if selection > len(selections):
            selection = 1  # loop if press down on last selection

    ansi("\033[?25h")  # show cursor

    os.system("cls" if os.name == "nt" else "clear")  # clear screen (cross platform)
    name: str = input("What is your name? ")

    ansi("\033[?1049l")  # go back to original screen

    return selection, name


def main():
    selection, name = menu()

    function_key: Dict[int, Callable] = {
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

    function = function_key.get(selection)  # get function corresponding to selection
    if function:
        function_call = lambda name: function(name)
        result = function_call(name)  # call function
        print(result)


if __name__ == "__main__":
    main()
