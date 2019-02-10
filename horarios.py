from datetime import date
import calendar
import os


def cabecalho():
    print('~' * 30)
    print(' ' * 6 + 'Escala de Horarios')
    print('~' * 30)
    print(' ' * 4 + '[1] Verificar data')
    print(' ' * 4 + '[2] Verificar mes')
    print(' ' * 4 + '[3] Verificar periodo')

    return int(input('Digite a opcao desejada: '))


def calculo():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))
    dt = date(ano, mes, dia)
    return dt.toordinal()


def verEscala(num):
    num = num % 8

    if num == 4 or num == 5:
        status = 'M'
        print('Horario manha')

    elif num == 6 or num == 7:
        status = 'M'
        print('Horario tarde')

    elif num == 0 or num == 1:
        status = 'M'
        print('Horario noite')

    elif num == 2 or num == 3:
        status = 'M'
        print('FOLGA')
    return status


def verEscalaMensal(num):
    num = num % 8

    if num == 4 or num == 5:
        status = 'M'
    elif num == 6 or num == 7:
        status = 'T'
    elif num == 0 or num == 1:
        status = 'N'
    elif num == 2 or num == 3:
        status = 'F'
    return status


def verificarMes(mes):
    ano = 2019
    dia = 1
    m, dFinal = calendar.monthrange(ano, mes)
    while dia < dFinal + 1:
        dt = date(ano, mes, dia)
        # print(dt.toordinal())
        statuss = verEscalaMensal(dt.toordinal())
        print(dia, '-', statuss)
        dia += 1


sair = 'S'
while sair != 'n' or sair != 'N':
    os.system('cls')
    opp = int(cabecalho())
    if opp == 1:
        dataOrdinal = calculo()
        verEscala(dataOrdinal)
    if opp == 2:
        m = int(input('Digite o mes:'))
        verificarMes(m)
    if opp == 2:
        pass
    sair = input('Deseja continuar? [S- Sim ] [N- Nao]')