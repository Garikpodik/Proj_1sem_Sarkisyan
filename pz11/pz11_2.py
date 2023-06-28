#Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое, количество букв в верхнем регистре. 
#Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.

# Чтение содержимого файла
with open("text18-22.txt", "r") as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

# Подсчет количества букв в верхнем регистре
uppercase_count = sum(1 for char in content if char.isupper())
print("Количество букв в верхнем регистре:", uppercase_count)

# Замена символов третьей строки их числовыми кодами
lines = content.split("\n")
if len(lines) >= 3:
    third_line = lines[2]
    new_third_line = ""
    for char in third_line:
        new_third_line += str(ord(char))
    lines[2] = new_third_line

# Формирование нового файла
new_content = "\n".join(lines)
with open("new_text.txt", "w") as file:
    file.write(new_content)
    print("Новый файл успешно создан.")