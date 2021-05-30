from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpResponseRedirect
import re
import polls.func as f


def index(request):
    if request.method == 'POST':
        warning_list = list()
        message = request.POST['message']
        key = request.POST['key']
        flag_crypt = int(request.POST['flag_crypt'])
        flag_action = request.POST['flag_action']
        response = str()
        no_key_crypt = [1,6,7,9,10,11,15] 

        if flag_crypt in no_key_crypt and key != '': # проверка на передачу ключа в те шифры, где это не нужно
            warning_list.append('Для данного шифра ключ не нужен. Игнорируем ключ')
        elif flag_crypt not in no_key_crypt and key == '':
            warning_list.append('Для данного шифра необходим ключ! Проверьте введенные данные')
            context = {
            'result': response,
            'warning_list' : warning_list
            }
            return render(request,'index.html',context= context)

        if flag_crypt == 1:
            response = f.atbash(message,flag_action)
        elif flag_crypt == 2:
            response = f.belazo(message,flag_action,key)
        elif flag_crypt == 3:
            response = f.caesar(message,flag_action,key)
        elif flag_crypt == 4:
            pass
        elif flag_crypt == 5:
            response = f.playfer(message,flag_action,key)
        elif flag_crypt == 6:
            response = f.reshetka_kardano(message,flag_action)
        elif flag_crypt == 7:
            response = f.polibiy(message,flag_action)
        elif flag_crypt == 8:
            pass
        elif flag_crypt == 9:
            response = f.a5_realisation(message,flag_action)
        elif flag_crypt == 10:
            response = f.a52_realisation(message,flag_action)
        elif flag_crypt == 11:
            response = f.rsa(message,flag_action)
        elif flag_crypt == 12:
            pass
        elif flag_crypt == 13:
            pass
        elif flag_crypt == 14:
            pass
        elif flag_crypt == 15:
            response = f.elgamal(message,flag_action)
        elif flag_crypt == 16:
            pass
        else:
            warning_list.append('Неправильно выбран шифр')
        context = {
            'result': response,
            'warning_list' : warning_list
        }
        return render(request,'index.html',context= context)
    else:
        return render(request,'index.html')
