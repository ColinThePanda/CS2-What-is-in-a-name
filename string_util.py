lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

def list_to_str(chars: list[str]) -> str:
    text = ""
    for char in chars:
        text += char
    return text


def remove_char(text: str, char: str) -> str:
    return list_to_str(list(filter(lambda x: x != char, text)))


def lower(text: str) -> str:
    upper_text = list_to_str(
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
    lower_text = list_to_str(
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
            space_locs.append(loc + 1)
    text += " "
    space_locs.append(-1)
    for i in range(len(space_locs) - 1):
        words.append(text[space_locs[i] : space_locs[i + 1]])
    return words
