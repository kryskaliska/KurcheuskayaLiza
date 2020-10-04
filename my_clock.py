from datetime import datetime
import time
import os
from mod_digit import dictionary

def get_current_time():      # get and return current time
    current_time = datetime.now().strftime('%H %M %S')
    return current_time

def print_digits(current_time):
    crt = str(current_time)
    hour1 = crt[0] 
    hour2 = crt[1]
    minutes1 = crt[3]
    minutes2 = crt[4]
    seconds1 = crt[6]
    seconds2 = crt[7]
    #for hour1, hour2, minutes1, minutes2, seconds1, seconds2 in dictionary:
    print(hour1,hour2,'  ',minutes1,minutes2,'  ',seconds1,seconds2)
    
def clear_screen(): #clear screen
    os.system('cls||clear')

def sleep_for_a_while(period): #delay between cycles
    time.sleep(0.3)

#x = True
#def separator_generator(_x):
#    while True:
#        print('\u2588')
#    _x = not _x
#    print(_x)
#    yield _x 
#x = separator_generator(x)

if __name__ == "__main__":
    while True:
        current_time = get_current_time()
        print_digits(current_time)
        clear_screen()
        sleep_for_a_while(0.3)