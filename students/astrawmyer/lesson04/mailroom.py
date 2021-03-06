#!/usr/bin/env python3

# new file for lesson 4 work

#donors = [["Manny Machado",[12.2,2.51,3.20]],["Adam Jones",[1024.14,22.21,323.45]],["Chris Davis",[3.2,5.55,4.20]]]
ddonors = {"Manny Machado": [12.2,2.51,3.20], "Adam Jones": [1024.14,22.21,323.45], "Chris Davis": [3.2,5.55,4.20]}


def display_list():    
    for name in ddonors.keys():
        print(name)

def write_letter(name,amount):
    line_one = 'Dear {},'.format(name)
    line_two = "Thank you for donating ${:.2f} to the Human Fund. Your money will be used appropriately.".format(amount)
    letter = line_one + "\n" + line_two
    return letter

def write_report(donors):
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*67)
    for i in donors:
        print('{1:27}${0:11.2f}{2:12}  ${3:12.2f}'.format(*i))



def thank_you():
    """Function to send a thank you letter."""
    while True:
        input_name = input("Enter full name: ")
        if input_name in ddonors.keys():
            donation = float(input("Enter donation amount:"))
            ddonors[input_name].append(donation)
            print(write_letter(input_name,donation))
            break
        elif input_name == 'list':
            display_list()
            
        else:
            print("Adding {} to donor database".format(input_name))
            donation = float(input("Enter donation amount:"))
            ddonors[input_name] = [donation]
            print(write_letter(input_name,donation))
            print(ddonors)
            break


def create_report():
    """Function to write a report of the donors."""
    donors_report = []
    for name, amount in ddonors.items():
        sum_donation = 0
        avg_donation = 0
        for i in amount:
            sum_donation = sum_donation + i
            num_donation = len(amount)
        avg_donation = sum_donation/num_donation
        #print(name, sum_donation, num_donation)
        donors_report.append([sum_donation, name, num_donation, avg_donation])
    donors_report.sort(reverse=True)
    write_report(donors_report)


def all_letters():
    """Function to write letters for everyone."""
    for name in ddonors:
        donation = ddonors[name][0]
        with open('{}.txt'.format(name), 'w') as f:
            f.write(write_letter(name, donation))
    print("Letter files created.")


if __name__ == "__main__":
    main_switch_function = {"1": thank_you, "2": create_report, "3": all_letters, "4": exit}
    while True:
        print("What do you want to do?")
        response = input("1. Send a Thank You, 2. Create a Report, 3. Send all letters, 4. Quit: ")
        main_switch_function.get(response)()