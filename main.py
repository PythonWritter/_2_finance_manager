import sys
import time

import collections
import json

class Functions():
    """ Main functions for writing data in file. """
    def __init__(self):
        pass

    def file_read(self, name):
        time.sleep(0.3)
        path = f'{name}.txt'
        file = open(path, 'r', encoding='utf-8')
        modif_line = file.read()
        modif_line = (modif_line.replace('{', ' '))
        modif_line = (modif_line.replace('}', ' '))
        modif_line = (modif_line.replace("'", " "))
        print(modif_line)
        file.close()

    def file_write(self, name, value):
        time.sleep(0.3)
        path = f'{name}.txt'
        file = open(path, 'w', encoding='utf-8')
        file.write(str(value))
        file.close()

    def special_write(self, name, dict_name):
        time.sleep(0.3)
        path = f'{name}.txt'
        file = open(path, 'w', encoding='utf-8')
        for key, value in dict_name.items():
            file.write(str(key) + ' --> ' + str(value) + '\n')
        file.close()

    def jsonload(self, json_name):
        """ json load: for dict load. """
        time.sleep(0.3)
        global purchase_complete
        with open(f'{json_name}.json', 'r') as f:
            purchase_complete = json.loads(str(f.read()))

    def jsondump(self, json_name):
        """ json load: for dict dump. """
        time.sleep(0.3)
        with open(f'{json_name}.json', 'w') as f:
            f.write(json.dumps(purchase_complete, indent=2))


functions = Functions()


class Visual_side(Functions):
    def __init__(self):
        super().__init__()
        pass

    """ Functions for class 'Main menu'. """
    def enter_data(self):
        """ Entering data for the purchase """
        self.date = str(input('Enter date : '))
        visual.enter_data_group()
        self.price = str(input('Enter price : '))
        self.comment = str(input('Enter comment : '))

    def enter_data_group(self):
        """ Group description """
        try:
            self.gr_name = int(input('\n' + 'Enter group icon' + '\n' + \
                                     ' 🛒   "Food"                      --> Press [1]\n' + \
                                     ' 👕   "Clothes"                   --> Press [2]\n' + \
                                     ' 💊   "Health | Pharmacy"         --> Press [3]\n' + \
                                     ' ＄   "Special | Big bill"        --> Press [4]\n' + \
                                     ' 💪   "My personal purchases"     --> Press [5]\n' + \
                                     ' 🎁   "Other"                     --> Press [6]\n' + \
                                     '\nMake your choice -->: '))
            if self.gr_name == 1:
                self.gr_name = 'Food.' + chr(128722)
            elif self.gr_name == 2:
                self.gr_name = 'Clothes.' + chr(128085)
            elif self.gr_name == 3:
                self.gr_name = 'Health.' + chr(128138)
            elif self.gr_name == 4:
                self.gr_name = 'Special.' + chr(65284)
            elif self.gr_name == 5:
                self.gr_name = 'Personal.' + chr(128170)
            elif self.gr_name == 6:
                self.gr_name = 'Other.' + chr(127873)
            else:
                pass
        except ValueError:
            print('Incorrect contribution!')
            print('You must enter an integer!')
            time.sleep(1.5)
            visual.enter_data_group()
        return self.gr_name

    def main_menu(self):
        """ Visual side of 'Main menu'. """
        selector = None
        try:
            selector = int(input('_' * 44 + '\n' + \
                                 '|___________________Menu___________________|\n' + \
                                 'Enter "1" if you want to add new product\n' + \
                                 'Enter "2" if you want to watch your records\n' + \
                                 'Enter "3" if you want to change a purchase\n' + \
                                 'Enter "4" if you want to delete a purchase\n' + \
                                 'Enter "5" view data by price "max" and "min"\n' + \
                                 'Enter "6" view data by groups\n' + \
                                 'Enter "7" save and exit\n' + \
                                 '*' * 44 + '\n' + \
                                 '\nMake your choice -->:'))
            if selector == 1:
                visual.p_1()
            elif selector == 2:
                visual.p_2()
            elif selector == 3:
                visual.p_3()
            elif selector == 4:
                visual.p_4()
            elif selector == 5:
                visual.p_5()
            elif selector == 6:
                visual.p_6()
            elif selector == 7:
                visual.p_7()
        except ValueError:
            print('Incorrect contribution!')
            print('You must enter an integer!\n')
            time.sleep(1.5)
            visual.main_menu()
        return selector

    def p_1(self):
        """ Menu p. № 1 'Add new product'. """
        print('Your last purchase was: ')
        functions.file_read('last_purchase')

        self.enter = int(input('Enter the next number of new purchase : '))
        visual.enter_data()
        if self.comment == '':
            d_purch = str(self.date + ' ' + str(self.gr_name) + ' ' + self.price)
        else:
            d_purch = str(self.date + ' ' + str(self.gr_name) + ' ' + self.price + ' ' + self.comment)

        one_purchase = d_purch
        one_purchase = one_purchase.split()

        purch_group = {}
        purch_group['Date'] = one_purchase[0]
        purch_group['Group'] = str(one_purchase[1])
        purch_group['Price  grn '] = int(one_purchase[2])
        if self.comment == '':
            pass
        else:
            purch_group['Comment: '] = str(one_purchase[3])
        print('\n', purch_group)

        functions.jsonload('data')

        purchase_complete[self.enter] = purch_group
        self.pur_com = purchase_complete

        functions.jsondump('data')

        functions.special_write('purchase', self.pur_com)

        [last] = collections.deque(purchase_complete, maxlen=1)
        functions.file_write('last_purchase', last)
        visual.return_end()

    def p_2(self):
        """ Menu p. № 2 'Watch your records'. """
        print('\n')
        functions.file_read('purchase')
        visual.return_end()

    def p_3(self):
        """ Menu p. № 3 'Change a purchase' """
        selector = None
        print('\nYour purchases: \n')
        functions.file_read('purchase')
        try:
            selector = str(input('\n' + '_' * 52 + '\n' + \
                                 'Please enter the purchase number you wish to change \n' + \
                                 '*' * 52 + '\n' + \
                                 '\nMake your choice -->: '))
        except ValueError:
            print('Incorrect contribution!')
            print('You must enter an integer!')
            visual.p_3()

        visual.enter_data()
        if self.comment == '':
            d_purch = str(self.date + ' ' + str(self.gr_name) + ' ' + self.price)
        else:
            d_purch = str(self.date + ' ' + str(self.gr_name) + ' ' + self.price + ' ' + self.comment)

        one_purchase = d_purch
        one_purchase = one_purchase.split()

        purch_group = {}
        purch_group['Date'] = one_purchase[0]
        purch_group['Group'] = one_purchase[1]
        purch_group['Price  grn '] = int(one_purchase[2])
        if self.comment == '':
            pass
        else:
            purch_group['Comment: '] = str(one_purchase[3])
        print(purch_group)

        functions.jsonload('data')

        purchase_complete[selector] = purch_group

        functions.jsondump('data')

        functions.special_write('purchase', purchase_complete)

        print('\nNow your shopping list looks like this: \n')
        functions.file_read('purchase')
        visual.return_end()

    def p_4(self):
        """ Menu p. № 4 'Delete a purchase'. """
        print('\nYour purchases: \n')
        functions.file_read('purchase')
        selector = str(input('\n' + '_' * 52 + '\n' + \
                             'Please enter the purchase number you wish to delete \n' + \
                             '*' * 52 + '\n' + \
                             '\nMake your choice -->: '))
        functions.jsonload('data')

        del purchase_complete[selector]

        functions.jsondump('data')

        functions.special_write('purchase', purchase_complete)

        print('\nNow your shopping list looks like this :\n')
        functions.file_read('purchase')
        visual.return_end()

    def p_5(self):
        """ Menu p. № 5 'max' and 'min'. """
        selector = int(input('\n' + '_' * 90 + '\n' + \
                             'If you want to to view data by price "max" and "min" for one day only --> Press [1] \n' + \
                             'If you want to to view data by price "max" and "min" for a period of days -->  Press [2] \n' + \
                             '*' * 90 + '\n' + \
                             '\nMake your choice -->: '))
        if selector == 1:
            visual.p_5_1()
        elif selector == 2:
            visual.p_5_2()
        else:
            pass
        visual.return_end()

    def p_5_1(self):
        """ Menu p. № 5.1 'One day only'. """
        print('\nYour purchases: \n')
        functions.file_read('purchase')
        selector = str(input('\n' + '_' * 85 + '\n' + \
                             'Please enter the date for which you want to see the amount of purchases on that day \n' + \
                             '*' * 85 + '\n' + \
                             '\nMake your choice -->: '))

        functions.jsonload('data')

        summa = []
        for values in purchase_complete.values():
            if values['Date'] == selector:
                summa.append(values['Price  grn '])

        print('\n1)All purchases made')
        print(selector, '\n', summa, '\n')

        print('2)Sorted purchase prices from min to max')
        print(sorted(summa), '\n')

        print('3)The biggest purchase on a given day: ')
        print(max(summa), ' grn\n')

        print('4)The lest amount of purchase on a given day: ')
        print(min(summa), ' grn\n')

        print('5)Sum of all purchases on a given date: ')
        print(sum(summa), ' grn')
        visual.return_end()

    def p_5_2(self):
        """ Menu p. № 5.2 'Period of days'. """
        print('\nYour purchases: \n')
        functions.file_read('purchase')
        print('\n')
        print('\n' + '_' * 85 + '\n' + \
              'Please, select the beginning and end of the specified period according to the numbers \n' + \
              '*' * 85 + '\n')
        selector_1 = int(input('First number of period: '))
        selector_1 -= 1
        selector_2 = int(input('Second number of period: '))

        functions.jsonload('data')

        all_summa = []
        for value in purchase_complete.values():
            all_summa.append(value['Price  grn '])

        all_summa = all_summa[selector_1:selector_2]

        print('\n1)All purchases made')
        print(all_summa, '\n')

        print('2)Sorted purchase prices from min to max')
        print(sorted(all_summa), '\n')

        print('3)The biggest purchase on a given day: ')
        print(max(all_summa), ' grn\n')

        print('4)The lest amount of purchase on a given day: ')
        print(min(all_summa), ' grn\n')

        print('5)Sum of all purchases on a given date: ')
        print(sum(all_summa), ' grn')
        visual.return_end()

    def p_6(self):
        """ Menu p. № 6 'View data by groups'. """
        print('\nYour purchases: \n')
        functions.file_read('purchase')
        visual.enter_data_group()

        functions.jsonload('data')

        summa = []
        for values in purchase_complete.values():
            if values['Group'] == self.gr_name:
                summa.append(values['Price  grn '])

        print('\n1)All purchases made in this group')
        print(self.gr_name)
        print(summa, '\n')

        print('2)Sorted purchase prices from min to max')
        print(sorted(summa), '\n')

        print('3)The biggest purchase on a given day: ')
        print(max(summa), ' grn\n')

        print('4)The lest amount of purchase on a given day: ')
        print(min(summa), ' grn\n')

        print('5)Sum of all purchases on a given date: ')
        print(sum(summa), ' grn')
        visual.return_end()


    def p_7(self):
        """ Menu p. № 7 'Save and exit'. """
        print('The program will be saved and closed')
        time.sleep(1)
        sys.exit()

    def return_end(self):
        """ Return, or finish the program. """
        selector = None
        try:
            selector = int(input('\n' + '_' * 52 + '\n' + \
                                 'If you want to go back to "Main menu" --> Press [1] \n' + \
                                 'If tou want to save and close the program --> Press [2] \n' + \
                                 '*' * 52 + '\n' + \
                                 '\nMake your choice -->: '))
            if selector == 1:
                visual.main_menu()
            elif selector == 2:
                print('Key "2" has been pressed. ')
                print('The program will be closed. ')
                time.sleep(1)
                sys.exit()
            else:
                pass
        except ValueError:
            print('Incorrect contribution!')
            print('You must enter an integer!')
            visual.return_end()
        return selector

visual = Visual_side()

if __name__ == '__main__':
    visual.main_menu()

