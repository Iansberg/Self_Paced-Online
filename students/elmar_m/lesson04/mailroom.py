#!/usr/bin/env python3

# def main():
#     answer = None
#     print(OPTS)
#     while answer != 'q':
#         answer = input('> ')
#         if answer == 't':
#             thankyou()
#         elif answer == 'r':
#             report()

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson04: Mailroom Exercise Part 2
'''

import time
import collections

# ts = time.strftime('%Y%m%d-%H%M%S') 

main_p = '\n> Main menu. Options: t == thankyou | r == report | q == quit program\n'
# sub_p = '\n>> Sub menu options: give me a donor name, or type "l" to see a list. Type "x" to exit.\n'
# sub_p = '\n>> Sub menu "thankyou". Options: l == list current donors | a == add new donor |  d == add donation | x == exit submenu\n'
sub_p = '\n>> Sub menu "thankyou". Options: l == list current donors | a == add donation / donor | x == exit submenu\n'

donors = collections.defaultdict(list)
 
donors['bill'] = [2000, 7.5, 950000]
donors['steve'] = [5.5, 234000, 928]
donors['donald'] = [657, 234, 28.57, 90456]
donors['angie'] = [2, 99, 297765, 47, 28346]
donors['kim'] = [38982, 66.23, 9856, 0.1]

def writefile(name, text):
    ts = time.strftime('%Y%m%d-%H%M%S')
    fname = '{}.{}.txt'.format(name, ts)
    f = open(fname, 'w')
    f.write(text)
    f.close

def mail(n, m):
    '''
    Create mail text.
    '''
    print('Dear {}, thank you very much for your donation of {} dollars.\n'.format(n, m))

def thankyou():
    '''
    Show list of known donors, add new donor to list, 
    add new donation to donor and print letter of thanks.
    '''
    menu(sub_p, sub_d)
    #name = None
    #while True:
    #    print('>> give me a donor name, or type "l" to see a list. Type "x" to exit.')
    #    name = input('>> ')
    #    if name == 'x':
    #        break
    #    elif name == 'l':
    #        print('\n'.join(donors))
    #    elif name in donors:
    #        print('>>', name, 'already in list')
    #        donation = input('>> please add current donation:\n>> ')
    #        donors[name].append(int(donation))
    #        print('>>', donation, 'added to donation list of', name, 'thank you.\n')
    #        mail(name, donation)
    #    elif not name in donors:
    #        print('>>', name, 'not in list, adding it ')
    #        donation = input('>> please add current donation:\n>> ')
    #        donors[name].append(int(donation))
    #        print('>>', donation, 'added to donation list of', name, 'thank you.\n')
    #        mail(name, donation)
    #print(prompt)

def list_donors():
    print('\n'.join(donors))
    
#def add_donor():
#    dname = input('>> Please give donor name to add: ')
#    amount = input('>> Please give donation amount: ')
#    donors[dname].append(int(amount))
#    print('>>', amount, 'added to donation list of', dname, 'thank you.\n')

# def add_donation():
def add():
    dname = input('>> Please give donor name: ')

    if dname in donors:
        print('>>', dname, 'already in list')

        # amount = input('>> please add current donation:\n>> ')
        # donors[dname].append(int(amount))
        add_amount(dname)

        # print('>>', donation, 'added to donation list of', name, 'thank you.\n')
        # mail(name, donation)
    elif not dname in donors:
        print('>>', dname, 'not in list, adding it ')

        # amount = input('>> please add current donation:\n>> ')
        # donors[dname].append(int(amount))
        add_amount(dname)

        # print('>>', donation, 'added to donation list of', name, 'thank you.\n')
        # mail(name, donation)
    # pass
    
def add_amount(donor):
    amount = input('>> please add current donation:\n>> ')
    donors[donor].append(int(amount))
    

def report():
    '''
    Show an overview of current donors and donations
    '''
    # get the highest number of digits to create formatstring accordingly:
    sumlist = []
    for i in donors.values():
        sumlist.append(sum(i))
    maxn = len(str(max(sumlist)))
    maxn += 2
    fstring = '{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' 
    print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
    print('-' * (maxn + 54)) 
    # for i in donors.keys():
    for i in donors:
        print(fstring.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) 
    #print(OPTS)
    # print(prompt)

def efunc():
    print('exiting.\n')
    return 'exiting'

'''
Dispatcher dictionary main menu
'''
main_d = {
    't' : thankyou,
    'r' : report,
    'q' : efunc,
    }

'''
Dispatcher dictionary submenu
'''
sub_d= {
    # 'l' : thankyou,
    'l' : list_donors,
    # 'a' : add_donor,
    'a' : add,
    'x' : efunc,
    }

#######################################################

def menu(p, d):
    '''
    Display menu to user. 
    This function uses a "dispatcher dictionary".

        ARGS:
    p:  prompt which is shown to the user
    d:  the dispatcher dictionary which holds the menu options
    '''
    try:
        while True:
            response = input(p)
            if d[response]() == 'exiting':
                break
    except KeyError:
        print('sorry, unknown option:', response)
        print(p)
        menu(p, d)
        # return None
    # finally:
    #     menu(p, d)



#######################################################
	
if __name__ == '__main__':
    menu(main_p, main_d)

