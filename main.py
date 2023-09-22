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
    
# 6 question -------------------------------------------------------------   
 
def n_comp_6(number):
    """
    Функція приймає число n та виконує з ним операцію n + nn + nnn
    >>>> n_comp(5)
    >> 615
    """
    return number + (number*10 + number) + (number*100 + number*10 + number)

# 10 question -------------------------------------------------------------

def dec_rand_10():
    '''Функція повертає випадкове число від 1 до 10 з 2 знаками після коми'''
    from random import random
    return round(random() * 10, 2)

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
        

# 18 question -------------------------------------------------------------

def tuple_reverse_18(tupl:tuple):
    '''функція приймає кортеж та повертає його розвернутим
    >>>> tuple_reverse_18((1,2,3,4,5))
    >> (5,4,3,2,1)'''
    return tupl[::-1]

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

