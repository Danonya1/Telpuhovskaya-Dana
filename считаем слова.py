text = input("Введите текст (от 5 слов с пробелами): ")
words = text.split()

# проверка на количество слов
if len(words) < 5:
    print("Введите текст, содержащий как минимум 5 слов.")
else:
    # подсчет частоты слов
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # поиск наиболее часто встречающегося слова и самого длинного слова
    most_common_word = max(word_counts, key=word_counts.get)
    longest_word = max(words, key=len)

    print(f"Наиболее часто встречающееся слово: {most_common_word}")
    print(f"Самое длинное слово: {longest_word}")
