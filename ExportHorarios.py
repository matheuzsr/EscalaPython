from datetime import date
import calendar
import os
import csv
import csv


anoInit= int(input('Digite o ano: '))
diaInit= int(input('Digite o primeiro horario manha: '))
#anoInit= 2020
#diaInit= 6
mesInit=1

#DADOS PROGRAMA
dt = date(year=anoInit,month=mesInit,day=diaInit)
i=dt.toordinal()
h=[[i%8,      'Horario manha','05:00 AM'],[(i+1)%8,  'Horario manha','05:00 AM'],[(i+2)%8,  'Horario tarde','10:00 AM'],[(i+3)%8,  'Horario tarde','10:00 AM'],[(i+4)%8,  'Horario noite','15:00 PM'],[ (i+5)%8,  'Horario noite','15:00 PM'],[(i+6)%8,  'Horario folga','08:00 AM'],[(i+7)%8,  'Horario folga','08:00 AM']]

#VERIFICANDO ULTIMO DIA DO ANO
endDay=date(year=anoInit,month=12,day=31).toordinal()

while(i < endDay):
    for item in h :
        if item[0]== i%8:
            print item[1],';',format(date.fromordinal(i), "%m/%d/%Y"),';',item[2]
    i+=1    