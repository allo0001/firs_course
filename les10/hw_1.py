# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). 
#Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.



class Matrix:
    
    def __init__(self, matrix):
        self.matrix =  matrix
        
        
    def __str__(self):
        return '\n\n'.join(['   '.join(map(str,i)) for i in self.matrix])
    
    
    def __add__(self, other):
        self.norm(*map(max, zip(self.get_size(), other.get_size())))
        other.norm(*map(max, zip(self.get_size(), other.get_size())))
        result = []
        for x in zip(m1.matrix, m2.matrix):
            result.append([sum(n)for n in zip(x[0],x[1])])
        return Matrix(result)
    
    
    def norm(self, i_n, j_n):
        if len(self.matrix) < i_n:
            for _ in range(j_n - len(self.matrix)):
                    self.matrix.append([])
        for i in self.matrix:
            if len(i) < j_n:
                for _ in range(j_n - len(i)):
                    i.append(0)
    
    def get_size(self):
        return len(self.matrix), max(len(x) for x in self.matrix)
            
    
    
m1 = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[1,2],[4,5],[7,8]])
print(m1)
print('*'*25)
print(m2)
print('*'*10 + 'Сумма' + '*'*10)
print(m1 + m2)
print('*'*40)
