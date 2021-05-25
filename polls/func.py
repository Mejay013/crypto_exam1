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


