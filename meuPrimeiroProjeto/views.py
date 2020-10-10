from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Ola')


def numbers(request, year):
    return HttpResponse('Ola numeros: ' + str(year))


def consult(request, name):
    res = solicitDataBase(name)
    # return HttpResponse('Mensagem automática: ' + name + res)
    return render(request, 'pessoa.html', {'v_res': res['text'], 'v_name': name, 'v_flag': res['flag']})


def solicitDataBase(name):
    names = ['Miguel', 'Helena', 'Marcia', 'Julia']
    if name in names:
        return {'text': ' ja existe', 'flag': True}
    return {'text': ' foi cadastrado com sucesso', 'flag': False}