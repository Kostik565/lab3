import numpy as np

def generate_matrix():
    return np.array([[np.random.randint(-10, 10) for j in range(4)] for i in range(3)])  #Генерація матриці

def work_which_matrix(a):
    numbers = a[a > 0] #Пошук елементів більших за 0
    M = np.sum(a < 0, axis=1) #Пошук кількості від'ємних елементів в кожному рядку
    even_columns = a[:, ::2] #Виведення парних стовпців матриці
    new_a = np.delete(a, [0], axis=0) #Видалення першого рядка
    return M, even_columns, new_a, numbers

def print_result(a, M, even_columns, new_a, numbers):
    print("Згенерована матриця:")
    print(a)
    for i in range(len(a)):
        print(f"В рядку {i+1} ({a[i]}) кількість від'ємних елементів: {M[i]}")
    
    print("\nСписок елементів, які більші за 0:", numbers)
    print("\nСтовпчики з парними індексами:")
    print(even_columns)
    print("\nМатриця після видалення першого рядка:")
    print(new_a)

def main():
    a = generate_matrix()
    M, even_columns, new_a, numbers = work_which_matrix(a)
    print_result(a, M, even_columns, new_a, numbers)

if __name__ == "__main__":
    main()