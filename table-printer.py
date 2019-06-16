# table-printer.py
# By Ben Bicakci
# Source: Automate the Boring Stuff by Al Sweigart

def print_table(list_table):
        
    col_widths = [0] * len(list_table)
        
    for widths in range(len(col_widths)):
        list_table[widths].sort(key=len)
        col_widths[widths] = len(list_table[widths][-1])
        # Originally, I was sorting each list from shortest to longest string,
        # and then passing the string length to col_widths, before sorting
        # col_widths and taking the largest value (8, 'cherries' from list_table[0][2]).
        # The problem is you need the largest string length value for each list/row
        # in list_table, so you justify each list based on that, not justify ALL lists
        # according the largest value in the WHOLE list_table (which causes your formatting
        # to look a bit different to the task in Ch.5 of Automate the Boring Stuff).

    for col in range(len(list_table[0])):
        print()
        for row in range(len(list_table)):
            print(list_table[row][col].rjust(col_widths[row]), end= ' ')
    
    print()      

table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)