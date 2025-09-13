import time
import random

def fill_matr(matr):
    for i in matr:
        for j in range(len(i)):
            i[j] = random.randint(-100, 100)

def matrix_multiply(A, B):
    # Получаем размеры матриц
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Проверяем возможность умножения
    if cols_A != rows_B:
        raise ValueError("Невозможно умножить матрицы: несовместимые размеры")
    
    # Создаем результирующую матрицу, заполненную нулями
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Выполняем умножение
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def test(razm):
    matrix_1 = [[0]*razm]*razm
    matrix_2 = [[0]*razm]*razm

    fill_matr(matrix_1)
    fill_matr(matrix_2)

    start = time.time()

    multiply = matrix_multiply(matrix_1, matrix_2)

    end = time.time()

    time_of_work = end - start
    print(f"время премножения матриц {razm}X{razm} составило {time_of_work} секунд")
    return time_of_work
    


rows_cols = [100]
while len(rows_cols)!=19:

    if rows_cols[len(rows_cols)-1]<1000:
        rows_cols.append(rows_cols[len(rows_cols)-1]+100)

    else: rows_cols.append(rows_cols[len(rows_cols)-1]+1000)

# print(rows_cols)


itogo = []

for i in rows_cols:
    if i==1000:break
    else:itogo.append(round(test(i), 5))
print(itogo)