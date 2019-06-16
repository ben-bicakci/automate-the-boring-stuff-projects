# password-strength-detector.py
# By Ben Bicakci
# Source: Automate the Boring Stuff by Al Sweigart
#
# This function uses regex to perform a strip() function. If the only argument
# passed to the function is the string to strip, whitespace characters
# will be removed from beginning and end of string. Otherwise, the specified
# characters in second argument will be removed

import re, pyperclip

str_to_strip = pyperclip.paste()
trg_chars = input("""Please enter the characters you want to strip, or leave blank to remove empty space from the beginning and end of the string. If you want to strip multiple characters please input them in list form (e.g., to strip all a, b, and c letter input: ['a', 'b', 'c']): """)

def regex_strip(user_str, strip_chars):
    if strip_chars == '':
        strip_chars_regex = re.compile(r'^\s|\s$')
    else:
        strip_chars_regex = re.compile(strip_chars)
    text_stripped = strip_chars_regex.sub('', user_str)
    return text_stripped

#regex_strip(str_to_strip, trg_chars)
print(regex_strip(str_to_strip, trg_chars))