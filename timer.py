import os
if os.name != 'nt':
    print("this app is only available on windows!\nexiting...")
    exit()
import time
import winsound
import random


# created by SpiritOfTheNight
# github : https://github.com/spiritofthenight/



time_format = '' # we determine if user input is in second or minute format !


# for colorizing the console always as green .
def start_color():
    os.system('color a')

# for colorizing the console randomly when the timer stop !
def colorize():
    color_list = [1,2,3,4,5,6,9]
    for c in color_list:
        return color_list[random.randint(1, 6)]

# for clearing the console .
def clear():
    os.system('cls')

# main timer function
def timer(usr_time):

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
    elif int(usr_time) > 60:

        while int(usr_time) > 0:
           
            passed = fixed_usr_time - int(usr_time)
            passed_min = passed // 60
            passed_sec = passed % 60

            remain_min = int(usr_time) // 60
            remain_sec = int(usr_time) % 60
            print(f"You setted the timer for: {fixed_usr_time} second, which equals to: {float((int(fixed_usr_time) / 60)):.02f} minutes") # pol this later
            print(f"\n| {passed_min}:{passed_sec:02d} passed | {remain_min}:{remain_sec:02d} is remaining ! |")
            #print(usr_time, ": usr time") 
            
            time.sleep(1)
            usr_time -= 1
            clear()

    

    # creating Sounds after the timer ends using Random numbers !:
    print('timer Stopped !\n')
    winsound.Beep(random.randint(800, 1500), 100)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 200)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 100)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 300)  # this part is for generating sound and randomly 
    os.system(f"color {colorize()}")               # and chaging txt color randomly
    winsound.Beep(random.randint(800, 1500), 300)  # when the timer stops ! pretty cool I guess !
    os.system(f"color {colorize()}")               # if I say it for myself !
    winsound.Beep(random.randint(800, 1500), 300)
    os.system(f"color {colorize()}")
    winsound.Beep(random.randint(800, 1500), 200)
    os.system(f"color {colorize()}")
    os.system(f"color a")



# Main Function :

def main():
    start_color()
    print('\n-- Big Boys Timer --\n')
    
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


# magic phrase !
if __name__ == "__main__":
    main()
