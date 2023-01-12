import matplotlib.pyplot as plt
import os
import datetime

day_list = ["SATURDAY","SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
def rainfall():
   rainfall_list = []
   for i in range (7):
       rainfall_daily = float(input(f"Enter the rainfall for {day_list[i]}: "))
       rainfall_list.append(rainfall_daily)
   return rainfall_list

rainfall_list = rainfall()
def min_max(rainfall_list):
   max_list = []
   min_list = []
   maximum = max(rainfall_list)
   minimum = min(rainfall_list)
   for i in range (7):
       if rainfall_list[i] == maximum:
           max_list.append(day_list[i])
       if rainfall_list[i] == minimum:
           min_list.append(day_list[i])
   print(f"The maximum rainfall is {maximum} and the minimum rainfall is {minimum}")
   return max_list, min_list

max_list, min_list = min_max(rainfall_list)

def show(max_list, min_list):
   print("The maximum rainfall is on day" , end = " " )
   for i in range (len(max_list)):
       print(max_list[i],",",end = " ")
   print()
   print("The minimum rainfall is on day" , end = " " )
   for i in range (len(min_list)):
       print(min_list[i],",",end = " ")
   print()

show(max_list, min_list)

def mean(rainfall_list):
   total = 0
   for i in range (7):
       total += rainfall_list[i]
   average = total/7
   return float(average)

#format decimal places 2 after the decimal point
mean = float(format(mean(rainfall_list),".2f"))

def above_mean(rainfall_list, mean):
   total = 0
   for i in range (7):
       square = (rainfall_list[i] - mean)**2
       total += square
   variance = float(total/7)
   standard_deviation = variance**0.5
   return standard_deviation

#2 decimal places
standard_deviation = float(format(above_mean(rainfall_list, mean),".2f"))

def visual():
    plt.bar(day_list,rainfall_list)
    plt.xlabel("Days")
    plt.ylabel("Rainfall")
    plt.title("Rainfall in a week(m.m)")
    for i in range(len(max_list)):
        plt.text(max_list[i],max(rainfall_list),f"(Max={max(rainfall_list)})")
    for i in range(len(min_list)):
        plt.text(min_list[i],min(rainfall_list),f"(Min={min(rainfall_list)})")
    plt.xticks(rotation=20)

    y_range = max(rainfall_list) - min(rainfall_list)

    plt.text(6, max(rainfall_list), f"Mean={mean}", bbox=dict(facecolor='red', alpha=0.5))
    plt.text(6, (max(rainfall_list)-(0.1*y_range)), f"St Dev={standard_deviation}", bbox=dict(facecolor='green', alpha=0.5))

    # Check if the folder already exists or not
    folder_name = "generated_image"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    now = datetime.datetime.now()
    current = now.strftime("%Y-%m-%d_%H-%M-%S")
    # save the figure in the generated_image folder
    file_name = f"figure{current}.png"
    plt.savefig(folder_name + '/' + file_name, dpi=300)

    plt.show()

def show_result(mean,standard_deviation):
   print(f"Mean is {mean}")
   print(f"The standard deviation is {standard_deviation}")

show_result(mean,standard_deviation)
visual()

