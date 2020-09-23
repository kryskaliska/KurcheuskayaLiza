creds = {'name1': 'pass1', 'name2': 'pass2'}
def auth_required(func):
    def wrapper(*args, **kwargs):
        print('Enter Login: ')
        name = input()
        print('Enter Password: ')
        passw = input()
        if (name, passw) in creds.items():
            value = func(*args, **kwargs)
            return value
        print('Authentication required')
        #return result
        # Do something after    
    return wrapper
@auth_required
def some_func(a, b):
    return (a + b)
print(some_func(10, 100))