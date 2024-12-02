import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

#Вывод столбца по названию
#print(df['Country name'])

#Вывод всей информации строки по индексу
#print(df.loc[56])

#Вывод определенной информации из строки по индексу и названию столбца
#print(df.loc[56, 'Healthy life expectancy'])

#Вывод по условию
print(df[df['Healthy life expectancy'] >0.7])