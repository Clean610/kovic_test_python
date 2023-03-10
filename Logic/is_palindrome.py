import re


def is_palindrome(word: str):
    word = re.sub('[^0-9a-zA-Z]+', '', word).lower()

    return word == word[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))
