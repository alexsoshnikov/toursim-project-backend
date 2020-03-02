# Пример реализации программы для 3 достопримечательностей
import pulp as p
import numpy as np

# создаем задачу оптимизации
LpProb = p.LpProblem('Problem', p.LpMaximize)
# X=[]

# Создаем переменные
x1_2 = p.LpVariable("x1_2", cat='Binary')
x1_3 = p.LpVariable("x1_3", cat='Binary')
x2_1 = p.LpVariable("x2_1", cat='Binary')
x2_3 = p.LpVariable("x2_3", cat='Binary')
x3_1 = p.LpVariable("x3_1", cat='Binary')
x3_2 = p.LpVariable("x3_2", cat='Binary')


x0_1 = p.LpVariable('x0_1', cat='Binary')
x0_2 = p.LpVariable('x0_2', cat='Binary')
x0_3 = p.LpVariable('x0_3', cat='Binary')

x1_0 = p.LpVariable("x1_0", cat='Binary')
x2_0 = p.LpVariable("x2_0", cat='Binary')
x3_0 = p.LpVariable("x3_0", cat='Binary')


c0 = p.LpVariable("c0", cat='Integer', lowBound=0)
c1 = p.LpVariable("c1", cat='Integer', lowBound=0)
c2 = p.LpVariable("c2", cat='Integer', lowBound=0)
c3 = p.LpVariable("c3", cat='Integer', lowBound=0)
n = 4


# x0
# print(X)
timeVizit = [60, 60, 60]  # время посещения достопримечательности
timeToGo = [[30, 40, 50],
            [30, 40, 50],
            [40, 40, 50],
            [30, 40, 50]]  # матрица времени в пути от i до j
timeVisit = [30, 60, 30, 90, 90, 120, 120,
             180, 180, 120, 180, 180, 120, 30, 30]
rating = [0, 4.7, 4.6, 4.9, 4.9, 4.3, 4.7, 4.3,
          4.9, 4.9, 4.7, 4.9, 4.5, 5.0, 5.0, 5.0]
price = [0, 700, 0, 300, 0, 400, 600, 5000, 500, 500, 400, 800, 750, 0, 0]

# Пишем целевую функцию
LpProb += rating[1]*x1_2 + rating[2]*x1_3 + rating[0]*x2_1 + rating[2]*x2_3 + \
    rating[0]*x3_1 + rating[1]*x3_2 + rating[0] * \
    x0_1 + rating[1]*x0_2 + rating[2]*x0_3

# Далее идут все ограничения
LpTotalTime = timeVizit[1]*x1_2 + timeVizit[2]*x1_3 + timeVizit[0]*x2_1 + timeVizit[2]*x2_3 + timeVizit[0]*x3_1 + timeVizit[1]*x3_2 + timeVizit[1]*x0_2 + \
    timeVizit[0]*x0_1 + timeVizit[2]*x0_3 + 30*x0_1 + 40*x0_2 + 50*x0_3 + 30*x1_0 + \
    40*x1_2 + 50*x1_3 + 40*x2_0 + 40*x2_1 + 50*x2_3 + 30*x3_0 + 40*x3_1 + 50*x3_2

LpProb += x0_2 + x1_2 + x3_2 == x2_1 + x2_3 + x2_0
LpProb += x0_3 + x1_3 + x2_3 == x3_1 + x3_2 + x3_0
LpProb += x0_1 + x2_1 + x3_1 == x1_2 + x1_3 + x1_0

LpProb += x0_2 + x1_2 + x3_2 <= 1
LpProb += x0_3 + x1_3 + x2_3 <= 1
LpProb += x0_1 + x2_1 + x3_1 <= 1

LpProb += x0_1 + x0_2 + x0_3 == 1
LpProb += x1_0 + x3_0 + x2_0 == 1
LpProb += c0 == 0

LpProb += c1 <= c0 + 1 - n*(x0_1 - 1)
LpProb += c1 >= c0 + 1 + n*(x0_1 - 1)
LpProb += c1 <= c2 + 1 - n*(x2_1 - 1)
LpProb += c1 >= c2 + 1 + n*(x2_1 - 1)
LpProb += c1 <= c3 + 1 - n*(x3_1 - 1)
LpProb += c1 >= c3 + 1 + n*(x3_1 - 1)

LpProb += c2 <= c0 + 1 - n*(x0_2 - 1)
LpProb += c2 >= c0 + 1 + n*(x0_2 - 1)
LpProb += c2 <= c1 + 1 - n*(x1_2 - 1)
LpProb += c2 >= c1 + 1 + n*(x1_2 - 1)
LpProb += c2 <= c3 + 1 - n*(x3_2 - 1)
LpProb += c2 >= c3 + 1 + n*(x3_2 - 1)

LpProb += c3 <= c0 + 1 - n*(x0_3 - 1)
LpProb += c3 >= c0 + 1 + n*(x0_3 - 1)
LpProb += c3 <= c1 + 1 - n*(x1_3 - 1)
LpProb += c3 >= c1 + 1 + n*(x1_3 - 1)
LpProb += c3 <= c2 + 1 - n*(x2_3 - 1)
LpProb += c3 >= c2 + 1 + n*(x2_3 - 1)

LpProb += LpTotalTime <= 2040

matr_c = [
    p.value(c0),
    p.value(c1),
    p.value(c2),
    p.value(c3)
]

matr_x = [
    [x0_1, x0_2, x0_3],
    [x1_0, x1_2, x1_3],
    [x2_0, x2_1, x2_3],
    [x3_0, x3_1, x3_2],
]

# LpProb +=
matrica = np.multiply(matr_x, timeToGo)
print(matrica)
print(sum(sum(matrica)))


print(LpProb)
status = LpProb.solve()
print(p.LpStatus[status])
print(p.value(x1_0), p.value(x0_2), p.value(
    c0), p.value(c1), p.value(c2), p.value(c3))
print(matr_c)


# print("timeToGo\n")
# index_i = 0
# while index_i <= 3:
#     index_j = 0
#     while index_j <=2:
#         print(timeToGo[index_i][index_j], ' = ', p.value(timeToGo[index_i][index_j]), '     ', sep = '', end = '')
#         index_j += 1
#     print()
#     index_i += 1


print("time VIzit\n", timeVizit)

print("matr_x\n")
index_i = 0
while index_i <= 3:
    index_j = 0
    while index_j <= 2:
        print(matr_x[index_i][index_j], ' = ', p.value(timeToGo[index_i][index_j])
              * p.value(matr_x[index_i][index_j]), '     ', sep='', end='')
        index_j += 1
    print()
    index_i += 1
print(p.value(LpTotalTime))
print(matr_c)


print(p.value(timeVizit[1]*x1_2 + timeVizit[2]*x1_3 + timeVizit[0]*x2_1 + timeVizit[2]*x2_3 +
              timeVizit[0]*x3_1 + timeVizit[1]*x3_2 + timeVizit[1]*x0_2 + timeVizit[0]*x0_1 + timeVizit[2]*x0_3))

print(p.value(30*x0_1 + 40*x0_2 + 50*x0_3 + 30*x1_0 + 40*x1_2 + 50 *
              x1_3 + 40*x2_0 + 40*x2_1 + 50*x2_3 + 30*x3_0 + 40*x3_1 + 50*x3_2))


matr_c = [
    p.value(c0),
    p.value(c1),
    p.value(c2),
    p.value(c3)
]

matr_x = [
    [x0_1, x0_2, x0_3],
    [x1_0, x1_2, x1_3],
    [x2_0, x2_1, x2_3],
    [x3_0, x3_1, x3_2],
]

print("matr_x\n")
index_i = 0
while index_i <= 3:
    index_j = 0
    while index_j <= 2:
        print(matr_x[index_i][index_j], ' = ', p.value(timeToGo[index_i][index_j])
              * p.value(matr_x[index_i][index_j]), '     ', sep='', end='')
        index_j += 1
    print()
    index_i += 1
