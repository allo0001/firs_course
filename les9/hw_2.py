class Road:
    
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height
        
    def weight(self):
        return self.__length * self.__width * self.__height * 25 // 1000
    
print(Road(5000, 20, 5).weight())
print(Road(50000, 100, 5).weight())        
print(Road(100, 100, 5).weight())        