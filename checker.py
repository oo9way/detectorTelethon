import re


def check(s):
    word_list = ["odam", "ketadigan", "oborib", "кетадиган", "pochta", "poshta", "пошта", "bor", "одам", "почта", "бор",
                 "ketish", "kishi",
                 "kerak", "кетиш", "керак", "ketishim", "ketmoqchi", "кетмоқчи", "кетмокчи" "edik", "едик", "едим",
                 "кетишим", "borish", "borishim", "боришим", "бориш", "пучта", "puchta", "po'chta", "powta", "po'wta"]

    black_list = ["юрамиз", "юраман", "yozish", "qo'shishingiz", "guruhda", "оламиз", "оламан", "yuramiz", "yuraman",
                  "olamiz", "olaman"]

    min_matches = []
    black_list_matches = []
    for text in s.split(" "):
        text = re.sub(r'[^a-zA-ZА-Яа-я]', '', text)

        if str(text).lower() in word_list:
            min_matches.append(text)

        if str(text).lower() in black_list:
            black_list_matches.append(text)

    if len(black_list_matches) != 0:
        return False

    if not len(min_matches) >= 2:
        return False

    return True
