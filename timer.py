import os
import time
import winsound
import random


# created by SpiritOfTheNight
# github : https://www.github.com/SpiritOfTheNight/



time_format = '' # we determine if user input is in second or minute format !

# to detect if the user is using windows only ! I will update it for posix systems later .
def detector():
    if not os.name == 'nt':
        print('this tool is only available on windows for now, sorry !')
        exit()


# for colorizing the console always as green .
def start_color():
    os.system('color a')

# for colorizing the console randomly when the timer stop ! good for when user do not have any sound device
def colorize():
    for c in range(1, 7):
        return random.randint(1, 6)

# for clearing the console .
def clear():
    os.system('cls')

# main timer function
def timer(usr_time):
    minute = 0
    second = 60
    minutes_left = int(usr_time) // 60
    seconds_left = int(usr_time) % 60
    seconds_passed = 0

    
    fixed_usr_time = int(usr_time)
    passed = fixed_usr_time - int(usr_time)
    passed_min = passed // 60
    passed_sec = passed % 60

    remain_min = int(usr_time) // 60
    remain_sec = int(usr_time) % 60

    fixed_usr_time = int(usr_time)
    if int(usr_time) == 0:
        print("\nYou cant set timer for zero seconds! try again !\n")
        return

    print(f'usr_time = {int(usr_time)}\n')
   
    if int(usr_time) <= 60:
        for t in range(1, int(usr_time)+1):
            print(f"you setted timer for : {usr_time} second ")
            print(f"\n| {t} second passed | {int(usr_time) - t} is remaining |")
            time.sleep(1)
            clear()
    

        while int(usr_time) > 0:
           
            passed = fixed_usr_time - int(usr_time)
            passed_min = passed // 60
            passed_sec = passed % 60

            remain_min = int(usr_time) // 60
            remain_sec = int(usr_time) % 60
            print(f"You setted the timer for: {fixed_usr_time} second, which equals to: {float((int(fixed_usr_time) / 60)):.02f} minutes") # pol this later
            print(f"\n| {passed_min}:{passed_sec:02d} passed | {remain_min}:{remain_sec:02d} is remaining ! |")
            
            
            time.sleep(1)
            usr_time -= 1
            clear()

    

    # creating Sounds after the timer ends using Random numbers in certian range :
    print('timer Stopped !\n')
    winsound.Beep(random.randint(800, 1500), 100)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 200)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 100)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 300)  
    os.system(f"color {colorize()}") 
    winsound.Beep(random.randint(800, 1500), 300)
    os.system(f"color {colorize()}")               
    winsound.Beep(random.randint(800, 1500), 300)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 200)
    os.system(f"color {colorize()}")
    os.system(f"color a")



# to detect if the user is using a windows device:
detector()




# Main Function :

def main():
    start_color()
    print("\n-- Big Boy's Timer --\n") # lol
    
    while True:
        try:
            form = input('what time format you would like to use?\n 1 = Second , 2 = minute\n I choose: ')
            if not form.isdigit():
                print('\nwrong Command ! only enter integers, try again !\n')
                continue
            time_format = f'{form}'
            print(f"\ntime_format is : {time_format}\n")

            user_command = input('\nplease Enter the time for timer: ')
            if not user_command.isdigit():
                print('Invalid Command ! only enter integers ! try again\n')
                continue
            if not time_format == '1':
                user_command = abs(int(user_command)) * 60
            timer(int(user_command))
            user_command2 = input('1 = set a new timer \n0 = exit\n enter the command: ')
            if not user_command2.isdigit():
                print('\ninvalid command ! only enter integers ! try again\n')
                continue
            if user_command2 == '1':
                continue
            elif user_command2 == '0':
                print("you exited the app!")
                break
            else:
                print("Unknown command ! only enter 1 or 0\nTry again: ")
                continue

        except KeyboardInterrupt as k:
            print(f"\n\napp exited with code 0 because of Keyboard Interruption")
            break


# magic phrase :
if __name__ == "__main__":
    main()
