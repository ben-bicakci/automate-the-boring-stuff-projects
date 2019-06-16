# collatz-sequence-1.0.py
# By Ben Bicakci
# Source: Automate the Boring Stuff with Python by Al Sweigart

def collatz(number):
    global val    
    if int(number) % 2 == 0:
        val = int(number) // 2
        print(val)
    if int(number) % 2 == 1:
        val = 3 * int(number) + 1
        print(val)

val = input('Please enter a number: ')

while val != 1:
    try:
        collatz(val)
    except ValueError:
        print('You did not enter a number.')
        val = input('Please enter a number: ')