from logging.config import listen

print("hello-world")

def square(list) -> list :
    list_squared = []
    for element in list :
        list_squared.append(element**2)
    return list_squared

list1 = [1,2,3,4,5,6,7,8]

print(square(list1))