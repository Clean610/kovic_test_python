def count_vowels(word: str):
    list_of_vowel = ["a", "e", "i", "o", "u"]
    count = 0

    for char in word:
        if char in list_of_vowel:
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowels("hello"))
