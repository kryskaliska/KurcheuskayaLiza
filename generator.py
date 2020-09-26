def my_gener(start):
    while True:
        if start % 3 == 0:
            print('Василий')
            start += 1
        yield start
        start += 1
g = my_gener(1)  
print(next(g))     
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g)) 
print(next(g))     
print(next(g)) 
print(next(g))  