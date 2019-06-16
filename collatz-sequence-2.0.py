# collatz-sequence-2.0.py
# By Ben Bicakci
# Source: Automate the Boring Stuff with Python by Al Sweigart

print('Enter number:')
num = input()

def collatz(n):
    try:
        n = int(n)
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            print(n)
    except ValueError:
        print('Please enter an integer')

collatz(num)