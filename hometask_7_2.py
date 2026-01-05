text = input("Enter a sentence: ")


def correct_sentence(text):
    text = text[0].upper() + text[1:]
    return text


if text[-1] != ".":
    text = text + "."

print(correct_sentence(text))
