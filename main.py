# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
import pandas
import pandas as pd
import matplotlib as plt

# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# Самостоятельно создайте DataFrame с данными
data = {
    'students': ["James", "Emily", "Michael", "Sarah", "William", "Jessica", "Daniel", "Elizabeth", "Matthew", "Olivia"],
    'maths': [3, 5, 4, 2, 4, 5, 3, 3, 4, 5],
    'literature': [2, 4, 3, 5, 5, 3, 4, 2, 4, 5],
    'biology': [5, 3, 5, 4, 2, 4, 3, 5, 3, 2],
    'history': [4, 2, 3, 5, 3, 5, 4, 4, 2, 5],
    'physics': [3, 5, 2, 4, 4, 3, 5, 2, 4, 3]
}

df = pandas.DataFrame(data)

# Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
print(df.head(3))

# Вычислите среднюю оценку по каждому предмету
print(f"\nСредние оценки сразу по всем предметам\n{df.mean(numeric_only=True)}")

# Вычислите медианную оценку по каждому предмету
print(f"\nМедианное значение оценок по всем предметам\n{df.median(numeric_only=True)}")

# Вычислите стандартное отклонение
print(f"\nСтандартное отклонение оценок по всем предметам\n{df.std(numeric_only=True)}")

# Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
Q1_maths = df['maths'].quantile(0.25)
Q3_maths = df['maths'].quantile(0.75)
print(f"\nПервый квантиль по математике: {Q1_maths}")
print(f"\nВторой квантиль по математике: {Q3_maths}")

# можно также попробовать рассчитать IQR
IQR = Q3_maths - Q1_maths
print(f"\nМежквартальный размах - {IQR}")
