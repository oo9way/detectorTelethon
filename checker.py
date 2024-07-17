import re


def check(s):
    word_list = ["одам бор", "почта бор", 'odam bor', 'pochta bor', 'кетиш керак', "ketish kerak"]

    if len(s) > 100:
        return False

    cleaned_text = ""

    for text in re.split(r'[ ,.\n]', s):
        text = re.sub(r'[^a-zA-ZА-Яа-я]', '', text)

        cleaned_text += text.lower() + " "

    for word in word_list:
        if word in cleaned_text:
            return True

    return False
