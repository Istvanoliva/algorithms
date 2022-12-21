def turn_into_dict(string):
    letters = dict()
    for character in string.lower():
        if character in letters:
            letters[character] += 1
        else:
            letters[character] = 1

    return letters


def turn_into_word(dict):
    sorted_word = ""
    while len(dict) > 0:
        letter = min(dict)
        for item in range(dict[letter]):
            sorted_word += letter
        del dict[f"{letter}"]

    return sorted_word


def is_anagram(first_string, second_string):
    first_dict = turn_into_dict(first_string.lower())
    second_dict = turn_into_dict(second_string.lower())

    first = turn_into_word(first_dict)
    second = turn_into_word(second_dict)
    comparison = first == second and first != ''

    return first, second, comparison
