from datetime import date
import calendar
import os
import cabecalho
import escala


sair = 'S'
while sair != 'n' or sair != 'N':
    os.system('cls')
    opp = int(cabecalho.Principal())
    
    if opp == 1:
        dataOrdinal = cabecalho.Calculo()
        escala.verEscala(dataOrdinal)

    if opp == 2:
        m = int(input('Digite o mes:'))
        escala.verificarMes(m)
        
    if opp == 2:
        pass

    sair = input('Deseja continuar? [S- Sim ] [N- Nao]')
