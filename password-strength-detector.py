# password-strength-detector.py
# By Ben Bicakci
# Source: Automate the Boring Stuff by Al Sweigart
#
# This program tests whether the password passed to it is strong (i.e.
# is at least eight characters long, has both uppercase and lowercase
# characters, and at least one digit).

import pyperclip, re

# Import password from clipboard

pw = pyperclip.paste()

def password_test(password):

# Detect whether eight char long
# Detect whether both uppercase and lowercase
# Detect whether at least one digit

    length_regex = re.compile(r'\S{8,99}?')
    lcase_regex = re.compile(r'[a-z]+')
    ucase_regex = re.compile(r'[A-Z]+')
    digit_regex = re.compile(r'\d+')

    pw_length = length_regex.search(password)
    pw_lcase = lcase_regex.search(password)
    pw_ucase = ucase_regex.search(password)
    pw_digit = digit_regex.search(password)

# Provide output stating whether password is strong or where it is
# weak if it fails specific password strength requirements

    if not pw_length:
        print('Your password is weak: Less than 8 characters.')
    if not pw_lcase:
        print('Your password is weak: No lowercase letter.')
    if not pw_ucase:
        print('Your password is weak: No uppercase letter.')
    if not pw_digit:
        print('Your password is weak: No numeric digit.')
    else:
        print('Your password is strong.')

password_test(pw)