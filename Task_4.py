word_list = []
marks_list = []
string = 'Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. Думаешь, им буду я? Нет. Это я постучу в дверь.'
words = string.split()


def string_list():
    for word in words:
        if word[-1] == '.' or word[-1] == ',' or word[-1] == '!' or word[-1] == '?':
            if word[-1] not in marks_list:
                marks_list.append(word[-1])

            if word[:-1] not in word_list:
                word_list.append(word[:-1])

        elif word[-1] != '.' or word[-1] != ',' or word[-1] != '!' or v[-1] != '?':
            if word not in word_list:
                word_list.append(word)


string_list()
print(word_list, marks_list)