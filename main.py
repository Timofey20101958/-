meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка",
            "ЩИЩ": "одобрение или восторг",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ": "злиться"
            }

while True:

    word = input("Введите непонятное слово (большими буквами!): ")

    if word in meme_dict.keys():
    # Что делать, если слово нашлось?
        print(word, "-", meme_dict[word])
    else:
    # Что делать, если слово не нашлось?
        print("данное слово не нашлось или написано не верно")
