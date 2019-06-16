# comma-code.py v1.0
# By Ben Bicakci
# Source: Automate the Boring Stuff with Python by Al Sweigart

users_list = ['item1', 'item2', 3, 'item4', 'item5', 'item6', 7, 'item8', 9]

def list_concatenator(users_list):
    
    items = len(users_list)
    
    if items == 0:
        return 'Your list is empty'

    elif items == 1:
        return "'" + str(users_list[0]) + "'"

    elif items == 2:
        return "'" + str(users_list[0]) + ' and ' + str(users_list[1]) + "'"

    else:      
        your_list_split1 = ', '.join((map(str,users_list[:-1])))
        return "'" + your_list_split1 + ', and ' + str(users_list[-1]) + "'"

list_concatenator(users_list)
print(list_concatenator(users_list))