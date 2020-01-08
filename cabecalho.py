from datetime import date
import calendar
import os

def Principal():
    print('~' * 30)
    print(' ' * 6 + 'Escala de Horarios')
    print('~' * 30)
    print(' ' * 4 + '[1] Verificar data')
    print(' ' * 4 + '[2] Verificar mes')
    print(' ' * 4 + '[3] Verificar periodo')

    return int(input('Digite a opcao desejada: '))

def Calculo():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))
    dt = date(ano, mes, dia)
    return dt.toordinal()