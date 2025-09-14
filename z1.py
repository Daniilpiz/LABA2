import time
import random

import matplotlib as plt

def shell(nums):
    inc = len(nums) // 2
    while inc:
        for i, el in enumerate(nums):
            while i >= inc and nums[i - inc] > el:
                nums[i] = nums[i - inc]
                i -= inc
            nums[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return nums

def built_in_sort(nums):
    return sorted(nums)

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

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
    
def draw(X, Y):
    plt.plot(X, Y)
    plt.xlabel("Размерности матриц")
    plt.ylabel("Время работы")
    plt.title("Перемножение матриц") 
    plt.show()


if __name__=="__main__":
    rows_cols = [100]
    while len(rows_cols)!=19:

        if rows_cols[len(rows_cols)-1]<1000:
            rows_cols.append(rows_cols[len(rows_cols)-1]+100)

        else: rows_cols.append(rows_cols[len(rows_cols)-1]+1000)

# print(rows_cols)


    itogo = []

    for i in rows_cols:
        if i==5000:break
        else:itogo.append(round(test(i), 5))

    print(itogo, sum(itogo)/3600)