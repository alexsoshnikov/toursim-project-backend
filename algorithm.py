import pulp as p
import numpy as np

coordinat = [
    "55.75371, 37.61988",
    "55.75252, 37.62308",
    "55.744525, 37.605281",
    "55.7262, 37.55639",
    "55.75116, 37.62872",
    "55.66766, 37.67069",
    "55.7942, 37.74907",
    "55.76013, 37.61864",
    "55.74138, 37.62086",
    "55.75533, 37.61784",
    "55.7473, 37.60511",
    "55.76323, 37.57659",
    "55.76144, 37.58365",
    "55.76015, 37.62469",
    "55.75489, 37.62158"
]


TimeToGo = [[0, 3, 20, 36, 8, 41, 36, 11, 21, 3, 19, 26, 31, 11, 3],
            [3, 0, 21, 37, 6, 44, 39, 15, 19, 6, 20, 31, 32, 14, 2],
            [20, 21, 0, 27, 20, 48, 43, 15, 20, 16, 5, 30, 30, 16, 18],
            [36, 37, 27, 0, 26, 64, 60, 32, 44, 32, 27, 42, 44, 32, 34],
            [8, 6, 20, 26, 0, 45, 40, 18, 20, 11, 17, 27, 28, 14, 7],
            [41, 44, 48, 64, 45, 0, 64, 39, 40, 39, 48, 52, 53, 42, 38],
            [36, 39, 43, 60, 40, 64, 0, 36, 47, 33, 41, 52, 54, 37, 33],
            [11, 15, 15, 32, 18, 39, 36, 0, 22, 8, 15, 28, 29, 6, 9],
            [21, 19, 20, 44, 20, 40, 47, 22, 0, 23, 21, 35, 35, 24, 20],
            [3, 6, 16, 32, 11, 39, 33, 8, 23, 0, 16, 27, 29, 10, 2],
            [19, 20, 5, 27, 17, 48, 41, 15, 21, 16, 0, 30, 29, 16, 18],
            [26, 31, 30, 42, 27, 52, 52, 28, 35, 27, 30, 0, 9, 22, 27],
            [31, 32, 30, 44, 28, 53, 54, 29, 35, 29, 29, 9, 0, 23, 28],
            [11, 14, 16, 32, 14, 42, 37, 6, 24, 10, 16, 22, 23, 0, 8],
            [3, 2, 18, 34, 7, 38, 33, 9, 20, 2, 18, 27, 28, 8, 0]]  # матрица времени в пути

rating = np.array([0, 4.7, 4.6,
                   4.9, 4.9, 4.3,
                   4.7, 4.3, 4.9,
                   4.9, 4.7, 4.9,
                   4.5, 5.0, 5.0, 5.0])  # рейтинг достопримечательности

priceVisit = [0, 0, 700, 0,
              300, 0, 400, 600,
              15000, 500, 500, 400,
              800, 750, 0, 0]  # стоимость посещения

priceToGo = [[0, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 0, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 0, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 0, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 0, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 0, 55, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 0, 55, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 0, 55, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 0, 55, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 55, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 55, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 55, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 55, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0, 55],
             [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 0]]  # матрица стоимости проезда

timeVisit = [0, 30, 60, 30,
             90, 90, 120, 120,
             180, 180, 120, 180,
             180, 120, 30, 30]  # время посещения достопримечательности


allTimeLimit = 11400  # значение для ограничения по суммарному времени
moneyLimit = 5600  # значение для ограничения по суммарным затратам
sightsLimit = 5  # значение для ограничения по суммарному времени
trTimeLimit = 11400  # значение для ограничения по суммарному времени
n = 15  # кол-во точек, ключая отель
start = n - 1  # точка, которая ближе всего к отелю


result = []
# Создание бинарных переменных X
X = []
for x in range(0, n):
    for i in range(0, x+1):
        X.append(p.LpVariable(name='x{}_{}'.format(x, i), cat='Binary'))
    for a in range(x+1, n):
        X.append(p.LpVariable(name='x{}_{}'.format(x, a), cat='Binary'))

# Преобразование списка в матрицу NxN
X = np.array([X])
X = X.reshape(n, n)


# Lprob=p.LpProblem('Максимизация посещенных достопримечательностей',p.LpMaximize)
# probl = 0
# for el in X:
#     for i in el:
#         probl += i
# Lprob += probl

Lprob = p.LpProblem('Минимизация времени', p.LpMinimize)
probl = 0
for i in X:
    probl += sum(timeVisit[:n]*i)
for i in range(n-1):
    probl += X[0][i+1] * TimeToGo[start-1][i] + \
        X[i+1][0] * TimeToGo[i][start-1]
for i in range(1, n):
    for j in range(1, n):
        probl += TimeToGo[i-1][j-1] * X[i][j]
Lprob += probl

# Создание переменных C
C = []
for u in range(0, n):
    C.append(p.LpVariable(name='c{}'.format(u), cat='Integer', lowBound=0))


# Ограничения


# Ограничение для выхода из отеля
sum0 = 0
for i in X[0]:
    sum0 += i

viiti = p.LpConstraint(sum0, sense=0, name='Вышел из отеля', rhs=1)
Lprob += viiti


# Ограничение для возвращения в отель
sum1 = 0
for x in X:
    sum1 += x[0]
voiti = p.LpConstraint(sum1, sense=0, name='Вернуться в отель', rhs=1)
Lprob += voiti


# Ограничение на суммарные затраты
total = priceVisit[:n]*X
probl = 0
for el in range(len(total)):
    for i in total[el]:
        probl += i
money = p.LpConstraint(
    probl, sense=-1, name='Денежное ограничение', rhs=moneyLimit)
#Lprob += money


# Ограничение на минимальное число посещенных достопримечательностей
minSight = 0
for el in X:
    for i in el:
        minSight += i
minVisit = p.LpConstraint(
    minSight, sense=1, name='Минимальное число посещенных', rhs=sightsLimit)
Lprob += minVisit


# Верхнее ограничение на суммарное время в транспорте
timeTr = 0
for i in range(n-1):
    timeTr += X[0][i+1] * TimeToGo[start-1][i] + \
        X[i+1][0] * TimeToGo[i][start-1]
for i in range(1, n):
    for j in range(1, n):
        timeTr += TimeToGo[i-1][j-1] * X[i][j]
upTimeTr = p.LpConstraint(
    timeTr, sense=-1, name='Суммарное время в транспорте', rhs=trTimeLimit)
Lprob += upTimeTr


# Ограничение на суммарное время
lpt = 0
lll = 0
for i in X:
    lpt += sum(timeVisit[:n]*i)
for i in range(n-1):
    lpt += X[0][i+1] * TimeToGo[start-1][i] + X[i+1][0] * TimeToGo[i][start-1]
for i in range(1, n):
    for j in range(1, n):
        lpt += TimeToGo[i-1][j-1] * X[i][j]


cons = p.LpConstraint(
    lpt, sense=-1, name='Ограничение на суммарное время', rhs=allTimeLimit)
Lprob += cons


Xt = X.transpose()
summa = 0

for i in range(0, n):
    for x in range(0, n):
        summa += X[i][x] - Xt[i][x]
    cons = p.LpConstraint(
        summa, sense=0, name='Вошёл - вышел{}'.format(i), rhs=0)
    summa, summa0 = 0, 0
    Lprob += cons
    cons = 0

# Начинаем в отеле
cons = p.LpConstraint(C[0], sense=0, name='Начинаем в отеле', rhs=0)
Lprob += cons


perem = 0
for j in range(1, n):
    for i in range(0, n):
        if i != j:
            perem = C[j] - (C[i]) + n*(X[i][j])
            cons = p.LpConstraint(
                perem, sense=-1, name='Единственность C{}_{} <='.format(j, i), rhs=n+1)
            Lprob += cons
            perem = C[j] - (C[i]) - n*(X[i][j])
            cons = p.LpConstraint(
                perem, sense=1, name='Единственность C{}_{} >='.format(j, i), rhs=-n+1)
            Lprob += cons

    # for i in range(j + 1,n):
    #     perem = C[j] - (C[i] + 1) + n*(X[i][j] - 1)
    #     cons = p.LpConstraint(perem,sense=-1,name='Единственность C{}_{} <='.format(j,i),rhs=0)
    #     Lprob += cons
    #     perem = C[j] - (C[i] + 1) - n*(X[i][j] - 1)
    #     cons = p.LpConstraint(perem,sense=1,name='Единственность C{}_{} >='.format(j,i),rhs=0)
    #     Lprob += cons


for j in range(1, n):
    perem = 0
    for i in range(0, n):
        perem += X[j][i]
    cons = p.LpConstraint(perem, sense=-1, name='One - one{}'.format(j), rhs=1)
    Lprob += cons


for i in range(0, n):
    perem = X[i][i]
    cons = p.LpConstraint(
        perem, sense=0, name='Диагональ{}_{}'.format(i, i), rhs=0)
    Lprob += cons

print(Lprob)  # Вывести всю задачу с ограничениями,переменными и целевой


status = Lprob.solve()
print(p.LpStatus[status])


for i in range(0, n):
    print('c{}='.format(i), p.value(C[i]), sep='')

print("0", end='->')

result.append(coordinat[start])

index = 1
while index != -1:
    chk = True
    for i in range(n):
        if p.value(C[i]) == index:
            print(i, end='->')
            result.append(coordinat[i-1])
            chk = False
            index += 1
            break
    if chk:
        index = -1

print("0")
result.append(coordinat[start])

print(result)

for el in X:
    for i in el:
        print(p.value(i), end=', ')
    print()
