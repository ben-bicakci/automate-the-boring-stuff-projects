# comma-code.py v1.1
# Revision 1
# By Ben Bicakci
# Source: Automate the Boring Stuff with Python by Al Sweigart

sequence = ['item1', 'item2', 3, 'item4', 'item5', 'item6', 7, 'item8', 9]

def list_concatenator(your_list):
     
     str_seq = list(map(str, your_list))

     try:
          if len(str_seq) == 1:
              return str_seq[0]
          
          elif len(str_seq) == 2:
               return f'{str_seq[0]} and {str_seq[1]}'

          else:      
            body = ', '.join(str_seq[:-1])
            return f'{body}, and {str_seq[-1]}'
     
     except:
          
          len(str_seq) == 0


list_concatenator(sequence)
print(list_concatenator(sequence))