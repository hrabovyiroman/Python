# 1 question-------------------------------------------------------------
floating_point = 3 + 5/8
print(f"Подання з плаваючою комою: {floating_point}")
integer_part = 3
print(f"ціле число: {integer_part}")

# 2 question -------------------------------------------------------------

def temperature_convert_2(degrees:float,type:str):
    '''Функція приймає градуси(float) і назву вимірної системи
      Цельсії- C , Фаренгейт - F  (заокруглення до 3 знаків після коми)
      >>>> temperature_convert_2(100,"F")
      >> 37.778
      >>>> temperature_convert_2(-50,"C")
      >> -58.0
      '''
    if type == 'F':
        return round((degrees - 32) * 5 / 9, 3)
    else:
        return round(degrees * 9 / 5 + 32, 3)

# 3 question ------------------------------------------------------------
def manipulate_integer_list():
    # Попросити користувача ввести список цілих чисел
    input_str = input("Enter a list of integers separated by spaces: ")
    
    # Перетворення вхідного рядка на список цілих чисел
    input_list = [int(x) for x in input_str.split()]

    # Print the last item in the list
    print("Last item in the list:", input_list[-1])

    # Надрукувати останній елемент у списку
    print("List in reverse order:", input_list[::-1])

    # Перевірте, чи список містить 5
    if 5 in input_list:
        print("Yes")
    else:
        print("No")

    # Вивести число п'ятірок у списку
    count_fives = input_list.count(5)
    print("Number of fives in the list:", count_fives)

    # Видаліть перший і останній елементи, відсортуйте елементи, що залишилися, і надрукуйте результат
    if len(input_list) >= 2:
        input_list.pop(0)  # Видалити перший елемент
        input_list.pop()   # Видалити останній елемент
        input_list.sort()
        print("List after removing first and last items and sorting:", input_list)
    else:
        print("List has less than 2 elements, cannot remove first and last items.")

    # Виведіть, скільки цілих чисел у списку менше 5
    count_less_than_5 = sum(1 for x in input_list if x < 5)
    print("Number of integers in the list less than 5:", count_less_than_5)

# Виклик функції для її виконання
manipulate_integer_list()


# 4 question -------------------------------------------------------------   

radius = float(input("Введіть радіус: "))
pi = 3.1415
area = round(pi * (radius ** 2), 3)
print("Площа кола буде - ", area, "см^2")

#5 question------------------------------------------------------------- 
first_name = input("Введіть своє імя: ")
last_name = input("Введіть ваше останнє імя: ")

full_name = last_name + " " + first_name
print("Ваше імя у зворотньому порядку:", full_name)

# 6 question -------------------------------------------------------------   

def n_comp_6(number):
    """
    Функція приймає число n та виконує з ним операцію n + nn + nnn
    >>>> n_comp(5)
    >> 615
    """
    return number + (number*10 + number) + (number*100 + number*10 + number)

# 7 question ------------------------------------------------------------
# Запитайте у користувача ціну страви та відсоток чайових
meal_price = float(input("Enter the price of the meal: $"))
tip_percentage = float(input("Enter the tip percentage you want to leave (e.g., 15 for 15%): "))

# Розрахуйте суму чайових
tip_amount = meal_price * (tip_percentage / 100)

# Обчисліть загальну суму рахунку, включаючи чайові
total_bill = meal_price + tip_amount

# Показати суму чайових і загальну суму рахунку
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Bill (including tip): ${total_bill:.2f}")

# 8 question -------------------------------------------------------------   

from datetime import datetime

print("Введіть, будь ласка, 3 числа: ")
day = int(input("День народження: "))
month = int(input("Місяць народження: "))
year = int(input("Рік народження: "))

today_date = datetime.now().date()
birthday_date = datetime(year, month, day).date()

total_number_of_days = (today_date - birthday_date).days
print(total_number_of_days, "днів - загальна кількість днів від народження.")

# 9 question  -------------------------------------------------------------
angle = float(input("Enter an angle between -180° and 180°: "))

angle = angle % 360
print("Equivalent angle between 0° and 360°:", angle)

# 10 question -------------------------------------------------------------

def dec_rand_10():
    '''Функція повертає випадкове число від 1 до 10 з 2 знаками після коми'''
    from random import random
    return round(random() * 10, 2)

    
# 12 question -------------------------------------------------------------  

credits_ = int(input("Скільки кредитів ви отримали? "))

if credits_ <= 23:
    print("Студент є першокурсником.")
elif 24 <= credits_ <= 53:
    print("Студенти є другокурсниками.")
elif 54 <= credits_ <= 83:
    print("Студент є юніор.")
else:
    print("Студент є старшокурсником.")

#13 question  -------------------------------------------------------------
centimeters = float(input("Введіть довжину в см: "))

if centimeters < 0:
    print("Довжина не може бути відємною.")
else:
    inches = centimeters / 2.54
    print(f"{centimeters} см = {inches:.2f} дюймів.")


# 14 question -------------------------------------------------------------

def rock_paper_scisors_14():
    def bot_choise():
        from random import choice
        global choises
        choises = ['rock', 'paper', 'scisors']
        return choice(choises)

    def main():
        choise = input('Введіть ваш вибір: ')
        bot = bot_choise()
        print(f'Вибір пк: {bot}')

        if choise == bot:
            return 0 
        elif choise == 'rock':
            if bot == 'paper':
                return -1
            return 1
        elif choise == 'paper':
            if bot == 'scisors':
                return -1
            return 1
        elif choise == 'scisors':
            if bot == 'rock':       
                return -1
            return 1
        else:
            print(f'Введіть свій вибіп з списку: {", ".join(choises)}')


    res = 0
    for i in range(3):
        print(f'{i+1} раунд')
        res += main()
    if res == 0:
        print('Нічия!')
    elif res > 0:
        print('Перемога!')
    else:
        print('Поразка')    

# 12 question -------------------------------------------------------------  

def johns_savings(N):
    beginning_savings = 300
    month_savings = 100
    every_six_month_savings = 500

    for month in range(1, N + 1):
        beginning_savings += month_savings
        if month % 6 == 0:
            beginning_savings += every_six_month_savings
    return beginning_savings


N = int(input("Введіть кількість місяців: "))

savings = johns_savings(N)
print(f"Заощадження Джона через {N} місяців становить ${savings}.")

# 18 question -------------------------------------------------------------

def tuple_reverse_18(tupl:tuple):
    '''функція приймає кортеж та повертає його розвернутим
    >>>> tuple_reverse_18((1,2,3,4,5))
    >> (5,4,3,2,1)'''
    return tupl[::-1]

# 20 question -------------------------------------------------------------

def remove_empty_strings(list_):
    result = []
    for i in list_:
        if i.strip():
            result.append(i)

    return result


input_list = ["Зима", "", "Весна", "", "Літо", "", "Осінь"]
filtered_list = remove_empty_strings(input_list)

for string in filtered_list:
    print(string)
    
# 22 question -------------------------------------------------------------

def profit_22(lst:list):
    '''
    Функція приймає список цін та повертає максимально можливий прибуток
    з 1 купівлі-продажу
    >>>> profit_22([2,5,6,4,1,3])
    >> 4
    '''
    if lst == lst.sort(reverse=True):
        return 0
    
    profit = 0
    
    for i in lst:
        minn = min(lst)
        n = lst.index(minn)
        maxx = max(lst[n:])
        lst.pop(n)
        if maxx - minn > profit:
            profit = maxx - minn
    return profit

# 26 question -------------------------------------------------------------

def anagram_check_26(s:str,t:str):
    '''Функція приймає два рядки і перевіряє чи вони є анограмами'''
    if len(s) != len(t):
        return False
    ls = []
    lt = []
    for i in range(1,len(s)+1):
        ls.append(s[-i])
        lt.append(t[-i])
    if sorted(ls) == sorted(lt):
        return True
    return False

# 30 question -------------------------------------------------------------

def mat_find_30(matrix:list,target:int):
    '''Функція перевіряє чи є число в матриці'''
    for i in matrix:
        if target in i:
            return True
    return False

