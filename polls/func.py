from re import findall # метод из модуля для разбиения строки на подстроки
import random
from math import gcd as bltin_gcd

result_a5 = str()
decrypt_resul_a5 = str()

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

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def rsa(message,flg):
    p = 3
    q = 7

    n = p*q
    eiler = (p-1)*(q-1)

    rand_list = [x for x in range(0,eiler) if x % 2 != 0 if coprime2(x,eiler) ]
    print (rand_list)

    d = 0
    e = 0

    for check in rand_list:
        for i in range(1000):
            if (i*check)%eiler == 1:
                d = i
                e = check

    pub_key = [e,n] # получение публичного ключа
    private_key = [d,n] # приватного публичного ключа


    check_key = lambda x,y: True if (y[0]**x[0])%eiler == 1 else False ## функция провреки ключа
    check1 = check_key(pub_key,private_key)



    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    if flg == 'encrypt':
        print_str = str()
        res = list()
        for i in message.upper():
            index = alphabet.index(i)
            res.append((index**pub_key[0])%pub_key[1])
        print_str = str(res).replace('[','').replace(']','')
        return print_str

    else:
        res = str()
        for i in message.split(','):
            index = (int(i)**private_key[0])%private_key[1]
            for check_index,symb in enumerate(alphabet):
                if check_index  == index :
                    res += symb
        return res

def a5_realisation(s,flg):
    global result_a5, decrypt_resul_a5
    default_len = int()
    if flg == 'encrypt':
        alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя.,-?!: "
        default_len = len(s)
        while len(s) % 8 != 0:
            randd = random.randint(0, 65)  # rand() % 65
            s2 = alph[randd]
            s = s + s2

        dva = [0] * 4500

        for i in range(0, len(s)):
            # 128 | | 64 | | 32 | | 16 | | 8 | | 4 | | 2 | | 1
            pos = alph.find(s[i])
            if pos >= 128:
                dva[i * 8 + 0] = 1
                pos = pos - 128
            if pos >= 64:
                dva[i * 8 + 1] = 1
                pos = pos - 64
            if pos >= 32:
                dva[i * 8 + 2] = 1
                pos = pos - 32
            if pos >= 16:
                dva[i * 8 + 3] = 1
                pos = pos - 16
            if pos >= 8:
                dva[i * 8 + 4] = 1
                pos = pos - 8
            if pos >= 4:
                dva[i * 8 + 5] = 1
                pos = pos - 4
            if pos >= 2:
                dva[i * 8 + 6] = 1
                pos = pos - 2
            if pos == 1:
                dva[i * 8 + 7] = 1

        krya = ""

        # Перевод сообщения в двоичный код
        for i in range(0, len(s) * 8):
            krya += str(dva[i])

        x2_code_text = "Двочный код сообщения:\n" + krya

        print_key = ""
        sh = [0] * 4500
        gamma = [0] * 64

        # Генерируем ключ
        for i in range(0, 64):
            randd = random.randint(0, 1)
            gamma[i] = randd
            print_key += str(gamma[i])
        gen_key = "Сгенерированный ключ:\n" + print_key

        for i in range(0, 4500):
            sh[i] = 0

        # Выработка гаммы
        for j in range(0, 4500):
            F = gamma[8] and gamma[29] or gamma[8] and gamma[51] or gamma[29] and gamma[51]
            if F == gamma[8]:
                zam = gamma[18] ^ gamma[17] ^ gamma[16] ^ gamma[13]
                gamma[18] = gamma[17]
                gamma[17] = gamma[16]
                gamma[16] = gamma[15]
                gamma[15] = gamma[14]
                gamma[14] = gamma[13]
                gamma[13] = gamma[12]
                gamma[12] = gamma[11]
                gamma[11] = gamma[10]
                gamma[10] = gamma[9]
                gamma[9] = gamma[8]
                gamma[8] = gamma[7]
                gamma[7] = gamma[6]
                gamma[6] = gamma[5]
                gamma[5] = gamma[4]
                gamma[4] = gamma[3]
                gamma[3] = gamma[2]
                gamma[2] = gamma[1]
                gamma[1] = gamma[0]
                gamma[0] = zam
            if F == gamma[29]:
                zam = gamma[40] ^ gamma[39]
                gamma[40] = gamma[39]
                gamma[39] = gamma[38]
                gamma[38] = gamma[37]
                gamma[37] = gamma[36]
                gamma[36] = gamma[35]
                gamma[35] = gamma[34]
                gamma[34] = gamma[33]
                gamma[33] = gamma[32]
                gamma[32] = gamma[31]
                gamma[31] = gamma[30]
                gamma[30] = gamma[29]
                gamma[29] = gamma[28]
                gamma[28] = gamma[27]
                gamma[27] = gamma[26]
                gamma[26] = gamma[25]
                gamma[25] = gamma[24]
                gamma[24] = gamma[23]
                gamma[23] = gamma[22]
                gamma[22] = gamma[21]
                gamma[21] = gamma[20]
                gamma[20] = gamma[19]
                gamma[19] = zam
            if F == gamma[51]:
                zam = gamma[63] ^ gamma[62] ^ gamma[61] ^ gamma[48]
                gamma[63] = gamma[62]
                gamma[62] = gamma[61]
                gamma[61] = gamma[60]
                gamma[60] = gamma[59]
                gamma[59] = gamma[58]
                gamma[58] = gamma[57]
                gamma[57] = gamma[56]
                gamma[56] = gamma[55]
                gamma[55] = gamma[54]
                gamma[54] = gamma[53]
                gamma[53] = gamma[52]
                gamma[52] = gamma[51]
                gamma[51] = gamma[50]
                gamma[50] = gamma[49]
                gamma[49] = gamma[48]
                gamma[48] = gamma[47]
                gamma[47] = gamma[46]
                gamma[46] = gamma[45]
                gamma[45] = gamma[44]
                gamma[44] = gamma[43]
                gamma[43] = gamma[42]
                gamma[42] = gamma[41]
                gamma[41] = zam
            # нахождение выходного бита
            sh[j] = gamma[18] ^ gamma[40] ^ gamma[63]

        print_gamma = ""
        for i in range(0, len(s) * 8):
            print_gamma += str(sh[i])

        gen_gamma = "Выработанная гамма:" + print_gamma

        # Шифруем текст в двоичном коде
        encrypt_dv_code = ""

        for i in range(0, int(len(s) / 8)):
            for j in range(0, 64):
                dva[j + i * 64] = dva[j + i * 64] ^ sh[j]
                encrypt_dv_code += str(dva[j + i * 64])

        shifr_text_x2 = "Зашифрованный текст (в двоичном виде):\n" + encrypt_dv_code
        result_a5 = encrypt_dv_code

        # Расишфровываем текст в двоичном коде
        decrypt_dv_code = ""

        print(len(s))

        for i in range(0, int(40 / 8)):
            for j in range(0, 64):
                dva[j + i * 64] = dva[j + i * 64] ^ sh[j]
                decrypt_dv_code += str(dva[j + i * 64])

        deshifr_text_x2 = "Расшифрованный текст (в двоичном виде):\n" + decrypt_dv_code

        # Переводи расшифрованный двоичный код в текст
        decrypt = ""
        for i in range(0, 40):
            # 128 | | 64 | | 32 | | 16 | | 8 | | 4 | | 2 | | 1
            pos = 0
            if dva[i * 8 + 0] == 1:
                pos = pos + 128
            if dva[i * 8 + 1] == 1:
                pos = pos + 64
            if dva[i * 8 + 2] == 1:
                pos = pos + 32
            if dva[i * 8 + 3] == 1:
                pos = pos + 16
            if dva[i * 8 + 4] == 1:
                pos = pos + 8
            if dva[i * 8 + 5] == 1:
                pos = pos + 4
            if dva[i * 8 + 6] == 1:
                pos = pos + 2
            if dva[i * 8 + 7] == 1:
                pos = pos + 1

            decrypt += str(alph[int(pos)])
        decrypt_resul_a5 =  decrypt[:default_len]
        return result_a5
    else:
        if s == result_a5:
            return decrypt_resul_a5

def a52_realisation(s,flg):
    global result_a5, decrypt_resul_a5
    alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"
    default_len = int()
    if flg == 'encrypt':
        default_len = len(s)
        while len(s) % 9 != 0:
            randd = random.randint(0, 65)
            s2 = alph[randd]
            s = s + s2

        dva = [0] * 5000
        for i in range(0, 5000):
            dva[i] = 0
        for i in range(0, len(s)):
            # 256||128||64||32||16||8||4||2||1
            pos = alph.find(s[i])
            if pos >= 256:
                dva[i * 9 + 0] = 1
                pos = pos - 256
            if pos >= 128:
                dva[i * 9 + 1] = 1
                pos = pos - 128
            if pos >= 64:
                dva[i * 9 + 2] = 1
                pos = pos - 64
            if pos >= 32:
                dva[i * 9 + 3] = 1
                pos = pos - 32
            if pos >= 16:
                dva[i * 9 + 4] = 1
                pos = pos - 16
            if pos >= 8:
                dva[i * 9 + 5] = 1
                pos = pos - 8
            if pos >= 4:
                dva[i * 9 + 6] = 1
                pos = pos - 4
            if pos >= 2:
                dva[i * 9 + 7] = 1
                pos = pos - 2
            if pos == 1:
                dva[i * 9 + 8] = 1

        # Перевод в двоичный код
        krya = ""
        for i in range(0, int(len(s) * 9)):
            krya += str(dva[i])
        x2_code_text = "Двочный код сообщения:\n" + krya

        # Генерация ключа
        print_key = ""
        sh = [0] * 5000
        gamma = [0] * 81
        for i in range(0, 81):
            randd = random.randint(0, 1)  # Рандом от 0 до 1
            gamma[i] = randd
            print_key += str(gamma[i])

        gen_key = "Сгенерированный ключ:\n" + print_key

        for i in range(0, 5000):
            sh[i] = 0

        # Выработка гаммы
        for j in range(0, 5000):
            F = gamma[67] * gamma[71] or gamma[71] * gamma[74] or gamma[74] * gamma[67]
            if F == gamma[8]:
                zam = gamma[18] ^ gamma[17] ^ gamma[16] ^ gamma[13]
                gamma[18] = gamma[17]
                gamma[17] = gamma[16]
                gamma[16] = gamma[15]
                gamma[15] = gamma[14]
                gamma[14] = gamma[13]
                gamma[13] = gamma[12]
                gamma[12] = gamma[11]
                gamma[11] = gamma[10]
                gamma[10] = gamma[9]
                gamma[9] = gamma[8]
                gamma[8] = gamma[7]
                gamma[7] = gamma[6]
                gamma[6] = gamma[5]
                gamma[5] = gamma[4]
                gamma[4] = gamma[3]
                gamma[3] = gamma[2]
                gamma[2] = gamma[1]
                gamma[1] = gamma[0]
                gamma[0] = zam

            if F == gamma[29]:
                zam = gamma[40] ^ gamma[39]
                gamma[40] = gamma[39]
                gamma[39] = gamma[38]
                gamma[38] = gamma[37]
                gamma[37] = gamma[36]
                gamma[36] = gamma[35]
                gamma[35] = gamma[34]
                gamma[34] = gamma[33]
                gamma[33] = gamma[32]
                gamma[32] = gamma[31]
                gamma[31] = gamma[30]
                gamma[30] = gamma[29]
                gamma[29] = gamma[28]
                gamma[28] = gamma[27]
                gamma[27] = gamma[26]
                gamma[26] = gamma[25]
                gamma[25] = gamma[24]
                gamma[24] = gamma[23]
                gamma[23] = gamma[22]
                gamma[22] = gamma[21]
                gamma[21] = gamma[20]
                gamma[20] = gamma[19]
                gamma[19] = zam

            if F == gamma[51]:
                zam = gamma[63] ^ gamma[62] ^ gamma[61] ^ gamma[48]
                gamma[63] = gamma[62]
                gamma[62] = gamma[61]
                gamma[61] = gamma[60]
                gamma[60] = gamma[59]
                gamma[59] = gamma[58]
                gamma[58] = gamma[57]
                gamma[57] = gamma[56]
                gamma[56] = gamma[55]
                gamma[55] = gamma[54]
                gamma[54] = gamma[53]
                gamma[53] = gamma[52]
                gamma[52] = gamma[51]
                gamma[51] = gamma[50]
                gamma[50] = gamma[49]
                gamma[49] = gamma[48]
                gamma[48] = gamma[47]
                gamma[47] = gamma[46]
                gamma[46] = gamma[45]
                gamma[45] = gamma[44]
                gamma[44] = gamma[43]
                gamma[43] = gamma[42]
                gamma[42] = gamma[41]
                gamma[41] = zam
                zam = gamma[80] ^ gamma[74]
                gamma[80] = gamma[79]

            zam = gamma[80] ^ gamma[74]
            gamma[80] = gamma[79]
            gamma[79] = gamma[78]
            gamma[78] = gamma[77]
            gamma[77] = gamma[76]
            gamma[76] = gamma[75]
            gamma[75] = gamma[74]
            gamma[74] = gamma[73]
            gamma[73] = gamma[72]
            gamma[72] = gamma[71]
            gamma[71] = gamma[70]
            gamma[70] = gamma[69]
            gamma[69] = gamma[68]
            gamma[68] = gamma[67]
            gamma[67] = gamma[66]
            gamma[66] = gamma[65]
            gamma[65] = gamma[64]
            gamma[64] = zam
            # нахождение выходного бита
            sh[j] = gamma[12] ^ gamma[14] ^ gamma[15] ^ gamma[18] ^ gamma[40] ^ gamma[35] ^ gamma[32] ^ gamma[28] ^ gamma[
                54] ^ \
                    gamma[57] ^ gamma[59] ^ gamma[63]

        print_gamma = ""
        for i in range(0, int(len(s) * 9)):
            print_gamma += str(sh[i])
        gen_gamma = "Выработанная гамма:\n" + print_gamma

        # Шифруем текст в двоичном коде
        encrypt_dv_code = ""

        for i in range(0, int(len(s) / 9)):
            for j in range(0, 81):
                dva[j + i * 81] = dva[j + i * 81] ^ sh[j]
                encrypt_dv_code += str(dva[j + i * 81])
        shifr_text_x2 = "Зашифрованный текст (в двоичном виде):\n" + encrypt_dv_code
        result_a5 = encrypt_dv_code

        # Расишфровываем текст в двоичном коде
        decrypt_dv_code = ""
        for i in range(0, int(len(s) / 9)):
            for j in range(0, 81):
                dva[j + i * 81] = dva[j + i * 81] ^ sh[j]
                decrypt_dv_code += str(dva[j + i * 81])

        deshifr_text_x2 = "Расшифрованный текст (в двоичном виде):\n" + decrypt_dv_code

        # Переводи расшифрованный двоичный код в текст
        decrypt = ""
        for i in range(0, len(s)):
            # 128||64||32||16||8||4||2||1
            pos = 0
            if dva[i * 9 + 0] == 1:
                pos = pos + 256
            if dva[i * 9 + 1] == 1:
                pos = pos + 128
            if dva[i * 9 + 2] == 1:
                pos = pos + 64
            if dva[i * 9 + 3] == 1:
                pos = pos + 32
            if dva[i * 9 + 4] == 1:
                pos = pos + 16
            if dva[i * 9 + 5] == 1:
                pos = pos + 8
            if dva[i * 9 + 6] == 1:
                pos = pos + 4
            if dva[i * 9 + 7] == 1:
                pos = pos + 2
            if dva[i * 9 + 8] == 1:
                pos = pos + 1
            decrypt += str(alph[int(pos)])
        decrypt_resul_a5 = decrypt[:default_len]
        return result_a5
    else:
        if s == result_a5:
            return decrypt_resul_a5

def playfer(text,flg,key):
    # инициализация алфавита
    alphavite_lower = ['а', 'б', 'в', 'г', 'д',
                       'е', 'ж', 'з', 'и', 'к',
                       'л', 'м', 'н', 'о', 'п',
                       'р', 'с', 'т', 'у', 'ф',
                       'х', 'ц', 'ч', 'ш', 'щ',
                       'ь', 'ы', 'э', 'ю', 'я']

    for krya in text:
        if krya == ',':
            text = text.replace(krya, 'зпт')
        elif krya == ".":
            text = text.replace(krya, "тчк")
        elif krya not in alphavite_lower:
            text = text.replace(krya, '')

    # Формируем алфавит
    new_alphabet = []  # Заготовка под новый алфавит

    for i in range(len(key)):
        new_alphabet.append(key[i])  # Заполняем новый алфавит значением ключа
    for i in range(len(alphavite_lower)):
        bool_buff = False  # Буфер для проверки вхождения символа в алфавит ниже
        for j in range(len(key)):
            if alphavite_lower[i] == key[j]:   # Если находим вхождение символа алфавита в ключ, то прерываем цикл и
                # переходим к другому символу
                bool_buff = True
                break
        if bool_buff == False:  # Если не нашли вхождение символа алфавита в ключ, то записываем его в новый алфавит
            new_alphabet.append(alphavite_lower[i])  # Заполняем алфавит
    print(" new_alphabet = {}".format(new_alphabet))

    # Формируем матричный алфавит
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            mtx_abt_i.append(new_alphabet[counter])  # Добавляем букву в матрицу
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print(" mtx_abt = ")
    for i in mtx_abt_j:
        print(i)
    # Поправляем текст
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    print(" text = {}".format(text))
    # Шифруем
    if flg == 'encrypt':
        enc_text = ""
        for t in range(0, len(text), 2):
            flag = True  # флаг для выхода из всех циклов
            for j_1 in range(5):
                if flag == False:
                    break
                for i_1 in range(6):
                    if flag == False:
                        break
                    if mtx_abt_j[j_1][i_1] == text[t]:
                        for j_2 in range(5):
                            if flag == False:
                                break
                            for i_2 in range(6):
                                if mtx_abt_j[j_2][i_2] == text[t + 1]:
                                    # Если буквы по диагонали
                                    if j_1 != j_2 and i_1 != i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][i_2] + mtx_abt_j[j_2][i_1]
                                    # Если буквы на одной строке
                                    elif j_1 == j_2 and i_1 != i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][(i_1 + 1) % 6] + mtx_abt_j[j_2][
                                            (i_2 + 1) % 6]  # %6 для предотвращения выхода за строку
                                    # Если буквы в одном столбце
                                    elif j_1 != j_2 and i_1 == i_2:
                                        enc_text = enc_text + mtx_abt_j[(j_1 - 1) % 5][i_1] + mtx_abt_j[(j_2 - 1) % 5][
                                            i_2]  # %5 для предотвращения выхода за столбец
                                    # Если буквы совпадают
                                    elif j_1 == j_2 and i_1 == i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][i_1] + mtx_abt_j[j_1][i_1]
                                    print(" {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                    flag = False
                                    break
        return enc_text
    else:
        enc_text = ""
        for t in range(0, len(text), 2):
            flag = True  # флаг для выхода из всех циклов
            for j_1 in range(5):
                if flag == False:
                    break
                for i_1 in range(6):
                    if flag == False:
                        break
                    if mtx_abt_j[j_1][i_1] == text[t]:
                        for j_2 in range(5):
                            if flag == False:
                                break
                            for i_2 in range(6):
                                if mtx_abt_j[j_2][i_2] == text[t + 1]:
                                    # Если буквы по диагонали
                                    if j_1 != j_2 and i_1 != i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][i_2] + mtx_abt_j[j_2][i_1]
                                    # Если буквы на одной строке
                                    elif j_1 == j_2 and i_1 != i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][(i_1 - 1) % 6] + mtx_abt_j[j_2][
                                            (i_2 - 1) % 6]  # %6 для предотвращения выхода за строку
                                    # Если буквы в одном столбце
                                    elif j_1 != j_2 and i_1 == i_2:
                                        enc_text = enc_text + mtx_abt_j[(j_1 + 1) % 5][i_1] + mtx_abt_j[(j_2 + 1) % 5][
                                            i_2]  # %5 для предотвращения выхода за столбец
                                    # Если буквы совпадают
                                    elif j_1 == j_2 and i_1 == i_2:
                                        enc_text = enc_text + mtx_abt_j[j_1][i_1] + mtx_abt_j[j_1][i_1]
                                    print(" {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                    flag = False
                                    break
        return enc_text
# ##################################### Вертикальная перестановка ##################################
def sortRow(keylen, badlist):
        k = key_len - 1
        while k > 0:
            ind = 0
            for j in range(k + 1):
                if badlist[0][j] > badlist[0][ind]:
                    ind = j
            for i in range(len(badlist)):
                m = badlist[i][ind]
                badlist[i][ind] = badlist[i][k]
                badlist[i][k] = m
            k -= 1
        for i in range(len(badlist)):
            for j in range(keylen):
                print("%4d" % badlist[i][j], end='')
                encrypted_matrix.append(badlist[i][j])
            print()

def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

def sortRowDec(keylen, badlist):
	k = keylen - 1
	while k > 0:
		ind = 0
		for j in range(k + 1):
			if badlist[0][j] > badlist[0][ind]:
				ind = j
		for i in range(len(badlist)):
			m = badlist[i][ind]
			badlist[i][ind] = badlist[i][k]
			badlist[i][k] = m
		k -= 1
		for i in range(len(badlist)):
			for j in range(keylen):
				print("%4d" % badlist[i][j], end='')
				decrypted_matrix.append(badlist[i][j])
			print()


def vertical_change(message,flg,key):
    alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
            'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
            'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
            'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
            'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
            'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
            'ю':30, 'я':31, ' ':32, ",":33, ".":34,
            'А':35, 'Б':36, 'В':37, "Г":38, "Д":39,
            'Е':40, 'Ж':41, 'З':42, 'И':43, 'Й':44,
            'К':45, 'Л':46, 'М':47, 'Н':48, 'О':49,
            'П':50, 'Р':51, 'С':52, 'Т':53, 'У':54,
            'Ф':55, 'Х':56, 'Ц':57, 'Ч':58, 'Ш':59,
            'Щ':60, 'Ъ':61, 'Ы':62, 'Ь':63, 'Э':64,
            'Ю':65, 'Я':66, '!':67, "?":68, ";":69}

    key = key
    key_len = len(key)
    print("Длина ключа:", key_len)
    msg = message
    while len(msg) < key_len * key_len:
        msg += '.'
    print("Длина фразы:", len(msg))
    msg_pl_key = key + msg
    list_msg = list(msg_pl_key)
    split_msg = [list_msg[i:i + key_len] for i in range(0, len(list_msg), key_len)]
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(split_msg[i][j], end=" ")
        print()
    coded = list()
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(int(alphabet_lower.get(split_msg[i][j])), end=" ")
            coded.append(int(alphabet_lower.get(split_msg[i][j])))
        print()
    split_coded = [coded[i:i + key_len] for i in range(0, len(coded), key_len)]
    # сортировка ключа и шифрование таблицы
    encrypted_matrix = list()
    print("\nЗашифрованная матрица: ")

    sortRow(key_len, split_coded)
    split_encrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]
    # print("Зашифрованный текст:", split_encrypted)
    print("\nЗашифрованный текст: ")


    for i in range(1, len(split_encrypted)):
        for j in range(0, len(split_encrypted[i])):
            print(get_key(alphabet_lower, split_encrypted[i][j]), end=" ")

    print("\n")
    # расшифровка
    decrypted_matrix = list()
split_decrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]
sortRowDec(key_len, split_decrypted)
decode = ""
print("\nРасшифровка:")
for i in range(1, len(split_msg)):
	for j in range(0, len(split_msg[i])):
		decode += split_msg[i][j] + " "
print(decode)
#print("Расшифрованный текст:", split_msg)


############################################## МАТРИЧНЫЙ ####################################################
