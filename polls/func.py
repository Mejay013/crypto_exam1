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

def s_block(message,flg):
    SBlocks = [[12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
           [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
           [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
           [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
           [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
           [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
           [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
           [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]


    alphavite = '0123456789abcdef'

    if flg == 'encrypt':
        text = message.encode('utf-8') #Ввод сообщения
        code = '' #Зашифрованное сообщение
        krya = 0

        #print(text.hex())
        for i in text.hex():
            code += alphavite[SBlocks[krya][alphavite.find(i)]]
        return code
    else:
        return ('Расшифровка не реализована')


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def group(iterable, count):
    """ Группировка элементов последовательности по count элементов """
 
    return list(zip(*[iter(iterable)] * count))

def elgamal(message,flg):
    p = 37
    g = 2
    x = 5
    y = (g**x)%p
    print(f' p = {p}, g = {g}, x = {x}')
    print(f'y = (g ^ x) mod p = {y}')

    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if flg == 'encrypt':
        message = message.upper()
        rand_list = list()
        for i in range(2,p-1):
            if IsPrime(i):
                rand_list.append(i)

        print(rand_list)
        
        encrypt_list = list()
        print(' a = (g ^ k)  mod p')
        print('b = ((y ^ rand_val ) * symb) mod p')
        for i in message:
            rand_val = random.choice(rand_list)
            a = (g**rand_val)%p
            b = (( y**rand_val ) * (alphabet.index(i)+1)) % p
            print(f' symb = {i}, n = {(alphabet.index(i)+1)}, k = {rand_val}, a = {a}, b = {b} ')
            encrypt_list.append([a,b])

        return encrypt_list
    else:
        encrypt_list = group([int(x) for x in message.replace('[','').replace(']','').split(',')],2)
        decrytp = str()
        for i in encrypt_list:
            index = ( i[1] * (i[0]**(p-1-x))  ) % p 
            decrytp += alphabet[index - 1]
        return decrytp.lower()