import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

#Выводит первые 5 строк. Кол-во строк можно изменить df.head(7)
#print(df.head)

#Выводит последние 5 строк. Кол-во строк можно изменить df.tail(7)
#print(df.tail)

#Выводит информацию
#print(df.info())

#Выводит стандартные статистические данные
print(df.describe())
