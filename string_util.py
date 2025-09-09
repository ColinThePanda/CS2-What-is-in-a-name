from typing import Dict

lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

def join(str: list[str], joiner : str = "") -> str:
    text = ""
    for i, str in enumerate(str):
        if i == len(str) - 1:
            text += str
        else:
            text += str + joiner
    return text


def remove_char(text: str, char: str) -> str:
    return join(list(filter(lambda x: x != char, text)))


def lower(text: str) -> str:
    upper_text = join(
        map(
            lambda let: (
                lowercase_letters[uppercase_letters.index(let)]
                if let in uppercase_letters
                else let
            ),
            text,
        )
    )
    return upper_text


def upper(text: str) -> str:
    lower_text = join(
        map(
            lambda let: (
                uppercase_letters[lowercase_letters.index(let)]
                if let in lowercase_letters
                else let
            ),
            text,
        )
    )
    return lower_text


def split_spaces(text: str) -> list[str]:
    words: list[str] = []
    space_locs: list[int] = [0]
    for loc, char in enumerate(text):
        if char == " ":
            space_locs.append(loc)
    for i in range(len(space_locs)):
        if i == len(space_locs) - 1:
            words.append(text[space_locs[i] + 1:])
        else:
            words.append(text[space_locs[i] : space_locs[i+1]])
    return words

def counter(text : str) -> Dict[str, int]:
    counts : Dict[str, int] = dict()
    for char in text:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts.update({char : 1})
    return counts

def mix_up_letters(text : str) -> str:
    from random import randint
    out_str = ""
    while len(text) > 0:
        index = randint(0, len(text) - 1)
        out_str += text[index]
        text = text[0 : index] + text[index + 1 :]
    return out_str