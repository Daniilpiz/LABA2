import time
import random

from matplotlib import pyplot as plt
def fill_mas(mas, var):
    if var == 1:
        for i in range(len(mas)):
            mas[i] = i
        return mas
    if var == 2:
        for i in range(len(mas)):
            mas[i] = len(mas) - i
        return mas
    if var == 3:
        for i in range(len(mas)):
            if i<len(mas)/2:
                 mas[i] = i
            else:
                mas[i] = len(mas) - i
        return mas
    if var == 4:
        for i in range(len(mas)):
            mas[i] = random.randint(-100, 100)
        return mas
    

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

def sortir(mas, var):
    if var == 1:
        return shell(mas)
    if var == 2:
        return built_in_sort(mas)
    if var == 3:
        return quicksort(mas)
    

def process_array(arr, fill_idx, result_list, time_list):
    arr = fill_mas(arr, fill_idx)
    for sort_type in [1, 2, 3]:
        start = time.time()
        sorted_arr = sortir(arr, sort_type)
        end = time.time()
            
        result_list.append(sorted_arr)
        time_list.append(end - start)

def sortirovki():
    c = [[0] * 10000 for _ in range(4)]
    d = [[0] * 30000 for _ in range(4)]

    result_1, time_1 = [], []
    result_2, time_2 = [], []

    # Обрабатываем массивы c
    for i in range(4):
        process_array(c[i], i + 1, result_1, time_1)

    # Обрабатываем массивы d
    for i in range(4):
        process_array(d[i], i + 1, result_2, time_2)
        
    return result_1, result_2, time_1, time_2

def draw(X, Y):
    plt.plot(X, Y)

    plt.xlabel("Размерности матриц")
    plt.ylabel("Время работы")

    plt.title("Перемножение матриц") 

    plt.show()

def main():
    choose = meet()
    if choose == 1:
        res_1, res_2, tim_1, tim_2 = sortirovki()
        print(f"""
Вид\Набор данных          Возрастающий               Убывающий             Возраст-убыв           Случайный
сортировки 

Сортировка Шелла           {tim_1[0]}                 {tim_1[1]}            {tim_1[2]}               {tim_1[3]}

Встроенная сортировка      {tim_1[4]}                 {tim_1[5]}            {tim_1[6]}               {tim_1[7]}

Быстрая Сортировка         {tim_1[8]}                 {tim_1[9]}            {tim_1[10]}              {tim_1[11]}                      
                                         
              """)
        
        print(f"""
Вид\Набор данных          Возрастающий               Убывающий             Возраст-убыв           Случайный
сортировки 

Сортировка Шелла           {tim_2[0]}                 {tim_2[1]}            {tim_2[2]}               {tim_2[3]}

Встроенная сортировка      {tim_2[4]}                 {tim_2[5]}            {tim_2[6]}               {tim_2[7]}

Быстрая Сортировка         {tim_2[8]}                 {tim_2[9]}            {tim_2[10]}              {tim_2[11]}                      
                                         
              """)
    if choose == 2:
        rows_cols = [100]
        while len(rows_cols)!=19:

            if rows_cols[len(rows_cols)-1]<1000:
                rows_cols.append(rows_cols[len(rows_cols)-1]+100)

            else: rows_cols.append(rows_cols[len(rows_cols)-1]+1000)

# print(rows_cols)


        itogo = []

        for i in rows_cols:
        # if i==1000:break
        # else:
            itogo.append(round(test(i), 5))

        print(itogo, sum(itogo)/3600)
        draw(rows_cols, itogo)

def meet():
    while True:
        print("Выберите сравнение сортировок(ввод 1) или перемножение матриц(ввод 2)\n")
        choose = int(input())
        if not (1<=choose<=2):
            print("Вы ввели не 1 или 2 повторите ввод")
        else: return choose


if __name__=="__main__":
    main()