def valid_parentheses(string: str) -> bool:
    """
    Checks if the parentheses in a given string are valid or not.
    :return: True if (([{}]))[], False if ((])
    """
    brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    brackets_stack = []

    for bracket in string:
        if bracket in brackets.keys():
            if (not brackets_stack) or (brackets_stack.pop() != brackets[bracket]):
                return False
        else:
            brackets_stack.append(bracket)
    return not brackets_stack

def count_letters_in_word_variations(word: str) -> dict:
    """
    Checks how many times each letter in a word is repeated in all variations of that word.
    https://mathematichka.ru/school/combinatorics/combination.html
    Variations of 'hello': ['hello', 'hell', 'hel', 'he', 'h', 'ello', 'ell', 'el', 'e', 'llo', 'll', 'l', 'lo', 'l', 'o']
    Get variations:
    for i in range(len(word)):
        for j in range(len(word), i, -1):
            new_word = word[i:j]
            words.append(new_word)
    :return: A dict of letters and their number of repetitions
    """
    letters = {letter: 0 for letter in word}

    for i, letter in enumerate(word, 1):
        sequence = i * (len(word) - i + 1)
        letters[letter] += sequence

    return letters