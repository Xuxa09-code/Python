#!/usr/bin/python3
totalSegundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = totalSegundos // (24*3600)
horas = (totalSegundos % (24*3600)) // 3600
minutos = ((totalSegundos % (24*3600)) % 3600) // 60
segundos = (((totalSegundos % (24*3600)) % 3600) % 60)
print(dias,'dias,', horas,'horas,',minutos,'minutos e', segundos,'segundos.')