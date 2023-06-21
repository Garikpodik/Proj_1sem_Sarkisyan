#Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
#Строка: --msg-template="SFileDirS) (path): (line): (column):(C):((symbol)) (msg)"


from string import punctuation

text = '--msg-template="SFileDirS) (path): (line): (column):(C):((symbol)) (msg)'
text_fin = ''.join([i for i in text if i in punctuation])  # нахождение цифр
print(text_fin)  # вывод результата