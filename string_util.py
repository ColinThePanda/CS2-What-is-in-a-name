from typing import Dict

lowercase_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
uppercase_letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def join(strs: list[str], joiner: str = "") -> str:
    """
    Joins a string into a list, with a given joiner between each item

    Args:
        strs (list[str]): list of strings to join
        joiner (str, optional): seperator/joiner. Defaults to "".

    Returns:
        str: joined string
    """
    text = ""
    for i, str in enumerate(strs):
        if i == len(strs) - 1:
            text += str  # do not add joiner if last item
        else:
            text += str + joiner
    return text


def remove_char(text: str, char: str) -> str:
    """
    Removes every instance of a given character from a string

    Args:
        text (str): text to remove a character from
        char (str): character to remove from text

    Returns:
        str: text with character removed
    """
    return join(list(filter(lambda x: x != char, text)))  # filter out character


def lower(text: str) -> str:
    """
    Returns the lowercase version of a string

    Args:
        name (str): input string

    Returns:
        str: lowercase string
    """
    lower_text = join(
        list(
            map(
                lambda let: (
                    lowercase_letters[uppercase_letters.index(let)]
                    if let in uppercase_letters
                    else let
                ),
                text,
            )
        )
    )
    return lower_text


def upper(text: str) -> str:
    """
    Returns the uppercase version of a string

    Args:
        name (str): input string

    Returns:
        str: uppercase string
    """
    upper_text = join(
        list(
            map(
                lambda let: (
                    uppercase_letters[lowercase_letters.index(let)]
                    if let in lowercase_letters
                    else let
                ),
                text,
            )
        )
    )
    return upper_text


def split(text: str, split: str = " ") -> list[str]:
    """
    Splits string into a list of sub-strings by a given character

    Args:
        text (str): text to split
        split (str, optional): character to split text by. Defaults to " ".

    Returns:
        sub-strings (list[str]): sub-strings when split by split character
    """
    words: list[str] = []
    split_locs: list[int] = [0]

    # get position of every instance of split char
    for loc, char in enumerate(text):
        if char == split:
            split_locs.append(loc)

    # split into sub strings
    for i in range(len(split_locs)):
        if i == len(split_locs) - 1:
            words.append(
                text[split_locs[i] + 1 :]
            )  # if last then do location to location to end
        elif i == 0:
            words.append(
                text[split_locs[i] : split_locs[i + 1]]
            )  # if firt then loc to next loc
        else:
            words.append(
                text[split_locs[i] : split_locs[i + 1]][1:]
            )  # last then loc to next loc excluding last char
    return words


def counter(text: str) -> Dict[str, int]:
    """
    Returns a dictionary containing every letter in a string and the number of instances of it in the string

    Args:
        text (str): string to count

    Returns:
        counter (Dict[str, int]): counter dictionary, {every letter in text : number of instances}
    """
    counts: Dict[str, int] = dict()
    for char in text:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts.update({char: 1})
    return counts


def mix_up_letters(text: str) -> str:
    """
    Shuffles characters in a string

    Args:
        text (str): string to shuffle

    Returns:
        str: shuffled string
    """
    from random import randint

    out_str = ""
    while len(text) > 0:
        index = randint(0, len(text) - 1)  # random index in text
        out_str += text[index]  # add text at index to out_str
        text = (
            text[0:index] + text[index + 1 :]
        )  #  remove char at index from text so not chosen again
    return out_str
