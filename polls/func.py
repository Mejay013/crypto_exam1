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

def RSA(message,flg):
    final_otvet = ""
    final_check = ""
    # Вычисление простых чисел #
    array = []
    flag = False
    for s in range(50, 1000):
        for i in range(2, s):
            if s % i == 0:
                flag = True
                break
        if flag == False:
            array.append(s)
        flag = False
    # array.append("...")
    final_otvet += "Простые числа (s):\n" + str(array) + '\n'

    # Простые числа
    p = int(random.choice(array))
    q = int(random.choice(array))
    final_otvet += "p = %d; q = %d\n" % (p, q)

    n = p * q  # Произведение
    Fn = (p - 1) * (q - 1)  # Функция Эйлера

    final_otvet += "n = %d; f(n) = %d\n" % (n, Fn)

    # Подбор открытой экспоненты #
    array2 = []
    for meow in range(2, 10000):
        d = int((1 + 2 * Fn) / meow)
        if d * meow == 1 + 2 * Fn:
            array2.append(meow)

    if array2 == []:
        final_otvet += "Невозможно найти взаимно простое число D!"
        raise SystemExit

    # array2.append("...")
    final_otvet += "Подходящие для открытой экспоненты числа(D): " + str(array2) + "\n"

    # Открытая экспонента
    D = int(random.choice(array2))  # Простое нечётное число не имеющее общих делителей с f(n)

    final_otvet += "Открытая экспонента (D) =" + str(D) + '\n'

    k = 2

    # Секретная экспонента
    E = int((1 + k * Fn) / D)

    final_otvet += "Секретная экспонента(E) =" + str(E) + "\n"

    # Условие на вычисление секретной экспоненты
    if E * D != 1 + k * Fn:
        raise SystemExit

    public_key = [D, n]  # Публичный ключ
    private_key = [E, n]  # Приватный ключ

    final_otvet += "Публичный ключ: " + str(public_key) + "\n"
    final_otvet += "Приватный ключ: " + str(private_key) + '\n'

    alphavit = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
                'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
                'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
                'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
                'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
                'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
                'ю': 30, 'я': 31, ' ': 32, ",": 33, ".": 34,
                'А': 35, 'Б': 36, 'В': 37, "Г": 38, "Д": 39,
                'Е': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44,
                'К': 45, 'Л': 46, 'М': 47, 'Н': 48, 'О': 49,
                'П': 50, 'Р': 51, 'С': 52, 'Т': 53, 'У': 54,
                'Ф': 55, 'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59,
                'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63, 'Э': 64,
                'Ю': 65, 'Я': 66, '!': 67, "?": 68, ";": 69}

    # Сообщение
    msg_list = list(message)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))
    final_otvet += "Длина исходного сообщения {} символов".format(len(alpha_code_msg)) + '\n'
    # print()

    def hash_value(n, alpha_code):
        i = 0
        hashing_value = 1
        while i < len(alpha_code_msg):
            hashing_value = (((hashing_value - 1) + int(alpha_code_msg[i])) ** 2) % n
            i += 1
        return hashing_value

    hash_code_msg = hash_value(p, alpha_code_msg)
    final_otvet += "Хэш сообщения (m):= {}".format(hash_code_msg) + '\n'

    m = hash_code_msg

    # Шифрование
    Cm = (m ** D) % n
    final_otvet += "Цифровая подпись (Cm): " + str(Cm) + '\n'

    # Расшифрование
    Dm = (Cm ** E) % n
    final_check += "Проверка цифровой подписи (Dm): " + str(Dm) + '\n'

    if m == Dm:
        final_check += str(m) + ' = ' + str(Dm) + '\n'
        final_check += "Подпись верна!" + '\n'
    else:
        final_check += str(m) + ' != ' + str(Dm) + '\n'
        final_check += "Подпись не верна!" + '\n'
    return final_otvet, final_check
"""
msg = input("Введите сообщение: ")
otvet = RSA_realisation(msg)
print(otvet[0], '\n', otvet[1])"""
