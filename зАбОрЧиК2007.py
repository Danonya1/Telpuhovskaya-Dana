s= input() #с клавы вводим строку
def alternate_case(string): #мы определяем функцию, которая принимает строку в качестве аргумента
    result = "" #пустая строка
    upper = False #лог переменная
    for char in string: #перебираем символы
        if char.isalpha(): #проверка является ли символ буквой
            if upper:
                result += char.upper() #верхний регистр
                upper = False
            else:
                result += char.lower() #нижний регистр
                upper = True
        else:
            result += char
    return result
print(alternate_case(s))
