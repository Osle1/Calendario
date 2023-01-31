import calendar, datetime
import sistema as st
import arquivos as aq

ano = datetime.datetime.today().year
mes = datetime.datetime.today().month
dia = datetime.datetime.today().day
horas = datetime.datetime.today().time().hour
minutos = datetime.datetime.today().time().minute
segundos = datetime.datetime.today().time().second

print(calendar.month(ano, mes))
print(calendar.month(ano, mes).replace(' 27 ', '[oi]'))

print(calendar.month(ano, mes).split(' '))

