from re import findall # метод из модуля для разбиения строки на подстроки
import random

def atbash(message, flag):
    alphavite = ',.!:\'\"#?@[](){} '
    if flag == 'encrypt':
        text = message
        code = ''  # Зашифрованное сообщение
        for i in text:  # блок шифрования
            if i.isupper():
                k = ord(i) % ord('А')  # находим позицию символа в алфавите (начиная с 0)
                code += chr(ord('Я') - k)  # выбираем из алфавита символ, который меньше на k+1 чем длина алфавита
            elif i.islower():
                k = ord(i) % ord('а')
                code += chr(ord('я') - k)
            else:
                code += alphavite[len(alphavite) - alphavite.find(i) - 1]
        return code  # Выводим зашифрованное сообщение
    else:
        text_decode = message
        global decode
        decode = ''
        for i in text_decode:  # блок расшифрования
            if i.isupper():
                k = ord(i) % ord('А')  # находим позицию символа в алфавите (начиная с 0)
                decode += chr(ord('Я') - k)  # выбираем из алфавита сивол, который меньше на k+1 чем длина алфавита
            elif i.islower():
                k = ord(i) % ord('а')
                decode += chr(ord('я') - k)
            else:
                decode += alphavite[len(alphavite) - alphavite.find(i) - 1]
        return decode

def belazo(message,flg,user_key):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    if flg == 'encrypt':
        text = message  # Ввод сообщения
        code = ''  # Зашифрованное сообщение
        key = user_key
        krya = 0

        for i in text:  # блок шифрования
            if i.islower():
                code += alphavite[(alphavite.find(i) + alphavite.find(key[krya]) + 1) % len(alphavite)]
            elif i.isupper():
                code += alphavite2[(alphavite2.find(i) + alphavite2.find(key[krya].upper()) + 1) % len(alphavite2)]
            else:
                code += alphavite3[(alphavite3.find(i) + alphavite3.find(key[krya]) - 1) % len(alphavite3)]
            krya = (krya + 1) % len(key)
        return code  # вывод зашифровнного текста
    else:
        decode = ''
        krya = 0
        code = message
        key = user_key
        for i in code:
            if i.islower():
                decode += alphavite[(alphavite.find(i) - alphavite.find(key[krya]) - 1) % len(alphavite)]
            elif i.isupper():
                decode += alphavite2[(alphavite2.find(i) - alphavite2.find(key[krya].upper()) - 1) % len(alphavite2)]
            else:
                decode += alphavite3[(alphavite3.find(i) - alphavite3.find(key[krya]) + 1) % len(alphavite3)]
            krya = (krya + 1) % len(key)

        return decode

def caesar(message,flg,key):
    alphavite = ',.!:\'\"#?@[](){} '
    alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = 'АБВГДДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЫЬЭЮЯ'
    if key == '':
        distance = 3
    else:
        distance = int(key)

    if flg == 'encrypt':
        code = str()
        plainText = message
        for i in plainText:
            if i.islower():
                code += alphavite1[(alphavite1.find(i) + distance) % len(alphavite1)]
            elif i.isupper():
                code += alphavite2[(alphavite2.find(i) + distance) % len(alphavite2)]
            else:
                code += alphavite[(alphavite.find(i) + distance) % len(alphavite)]
        return code
    else:
        code = message
        decode = str()
        for i in code:
            if i.islower():
                decode += alphavite1[(alphavite1.find(i) - distance) % len(alphavite1)]
            elif i.isupper():
                decode += alphavite2[(alphavite2.find(i) - distance) % len(alphavite2)]
            else:
                decode += alphavite[(alphavite.find(i) - distance) % len(alphavite)]
        return decode


def polibiy(message,flg):
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #алфавит
    if flg == 'encrypt':
        text = message #.lower() #Ввод сообщения
        encode = '' #Зашифрованное сообщение
        for i in text: #блок шифрования
            encode += str(alphavite.find(i) // 8 + 1) + str(alphavite.find(i) % 8 + 1) + ' '
                # определяем 2 числа, номер строки, как целое от деления позиции символа
                # в алфавите на 8, и номер столбца, как остаток от деления позиции символа на 8
        return encode #вывод зашифровнного текста
    else:
        text = message.split()
        decode = ''
        for i in text:
                decode += alphavite[(int(i[0]) - 1) * 8 + int(i[1]) - 1]
        return decode
        
def reshetka_kardano(message,flg):
    matrix_number = 1
    text = 'волккаждыйгодлиняетзптдавсесербываеттчк'
    SIZE = 4
    # дополняем матрицу с текстом до полной матрицы
    open_text_ = text
    if len(text) % (SIZE * SIZE) != 0:
        add_number = SIZE * SIZE - len(text) % (SIZE * SIZE)
        for i in range(add_number):
            text = text + "*"
    # определяем количество матриц
    if len(text) / (SIZE * SIZE) != 1:
        matrix_number = int(len(text) / (SIZE * SIZE))
    # print(" Введите значения ячеек решётки Кардано (0 - заполнена, 1 - пустота):\n")

    # формируем решётку Кардано
    bin_matrix = [[0 for x in range(SIZE)] for y in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            bin_matrix[i][j] = random.randint(0, 1)   # рандомизируем ячейки матрицы, либо 1, либо 0

    # формируем матрицу с текстом
    text_matrix = [[[0 for x in range(SIZE)] for y in range(SIZE)] for matrix in range(matrix_number)]
    counter_text = 0  # счётчик позиции символа в тексте
    for i in range(matrix_number):
        for j in range(SIZE):
            for k in range(SIZE):
                text_matrix[i][j][k] = text[counter_text]
                counter_text += 1
    if flg == 'encrypt':
        # шифрование
        # SIZE - размерность матрицы, z - номер матрицы с текстом, i - строка (Y), j - столбец (X).
        enc_text = ""
        for z in range(matrix_number):
            # прямой обход решетки
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[i][j] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 90 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - j - 1][i] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 180 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
            # поворот решетки на 270 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[j][SIZE - i - 1] == 1:
                        enc_text = enc_text + text_matrix[z][i][j]
        encrypted_text = str((" {}\n".format(enc_text)))
        return enc_text
        # расшифрование
    else:
        enc_text = message
        # формируем матрицу с текстом
        text_matrix = [[[0 for x in range(SIZE)] for y in range(SIZE)] for matrix in range(matrix_number)]
        counter_text = 0  # счётчик позиции символа в тексте
        for i in range(matrix_number):
            for j in range(SIZE):
                for k in range(SIZE):
                    text_matrix[i][j][k] = enc_text[counter_text]
                    counter_text += 1
        open_text = ""
        for z in range(matrix_number):
            # прямой обход решетки
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[i][j] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 90 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - j - 1][i] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 180 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                        open_text = open_text + text_matrix[z][i][j]
            # поворот решетки на 270 градусов по часовой стрелке
            for i in range(SIZE):
                for j in range(SIZE):
                    if bin_matrix[j][SIZE - i - 1] == 1:
                        open_text = open_text + text_matrix[z][i][j]
        decrypted_text = str(" {}\n".format(open_text_))
        return  decrypted_text
