from datetime import date
import calendar
import os

def verEscala(num):
    num = num % 8

    if num == 4 or num == 5:
        status = 'F'
        print('FOLGA')

    elif num == 6 or num == 7:
        status = 'M'
        print('Horario manhã')

    elif num == 0 or num == 1:
        status = 'T'
        print('Horario tarde')

    elif num == 2 or num == 3:
        status = 'N'
        print('Horario noite')
    return status


def verEscalaMensal(num):
    num = num % 8

    if num == 4 or num == 5:
        status = 'F'
    elif num == 6 or num == 7:
        status = 'M'
    elif num == 0 or num == 1:
        status = 'T'
    elif num == 2 or num == 3:
        status = 'N'
    return status   


def verificarMes(mes):
    ano = 2019
    dia = 1
    m, dFinal = calendar.monthrange(ano, mes)
    while dia < dFinal + 1:
        dt = date(ano, mes, dia)
        # print(dt.toordinal())
        statuss = escala.verEscalaMensal(dt.toordinal())
        print(dia, '-', statuss)
        dia += 1