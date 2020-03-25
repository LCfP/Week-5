leet_speak = {
    "l": "1",
    "e": "3",
    "a": "4",
    "o": "0",
}


def replace_dictionary(text, dictionary):
    for key in dictionary:
        text = text.replace(key, dictionary[key])
    return text


with open("exercise_1_input.txt") as input_file:
    input_text = input_file.read()

print(replace_dictionary(input_text, leet_speak))
