
# Получаем алфавит на английском языке
# Алфавит с первым пробелом
alphabets_in_lowercase = [' ']
for i in range(97, 123):
    # Заполняем его символами, обращаясь к ним по коду
    alphabets_in_lowercase.append(chr(i))


print('Текущий алфавит: ' + str(alphabets_in_lowercase))
crypto = str(input('Введите строку для шифрования: '))
crypto_position = int(input('Укажите позицию смещения алфавита: '))

# Преобразуем введённую строку в нижний регистр
crypto_string = crypto.lower()
# crypto_string = crypto_string.replace(" ", "")

print('Строка для шифрования: ' + crypto_string)

crypto_array = list(crypto_string)

array_after_crypto = []

for i in range(0, len(crypto_array)):
    new_crypto_index = alphabets_in_lowercase.index(crypto_array[i])
    if new_crypto_index < len(alphabets_in_lowercase) - crypto_position:
        array_after_crypto.append(alphabets_in_lowercase[new_crypto_index + crypto_position])
    else:
        array_after_crypto.append(alphabets_in_lowercase[0 + crypto_position])

string_after_crypto = ''.join(array_after_crypto)
print('Шифрованная строка ' + string_after_crypto)

print("Введите 1, если надо выполнить дешифрование, иначе введите 0")
flag = int(input())

crypto_array = array_after_crypto
print(array_after_crypto)
array_after_de_crypto = []
if flag == 1:
    for i in range(0, len(crypto_array)):
        new_crypto_index = alphabets_in_lowercase.index(crypto_array[i])
        # if new_crypto_index < len(alphabets_in_lowercase) - crypto_position:
        array_after_de_crypto.append(alphabets_in_lowercase[new_crypto_index - crypto_position])
    string_after_de_crypto = ''.join(array_after_de_crypto)
    print('Дешифрованная строка: ' + string_after_de_crypto)
    print('Дешифрование завершено')
else:
    exit('Шифрование завершено')
