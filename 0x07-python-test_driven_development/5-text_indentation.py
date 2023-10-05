#!/usr/bin/python3
'''
This Module has a function that prints text
'''


def text_indentation(text):
    '''This function prints name (<first name> <last name>)

    Args:
        text (str): Text to be printed

    Raises:
        TypeError: If text is not a strings
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    delim = False

    for i in text:
        if i in [".", ":", "?"]:
            result += i + "\n\n"
            delim = True
        elif i.isspace() and delim:
            continue
        else:
            result += i
            delim = False

    result = result.strip()
    print(result)
    print()
